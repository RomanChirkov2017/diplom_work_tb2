from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.test import TestCase

from education.models import EducationModule, Lesson
from education.serializers import EducationModuleSerializer, LessonSerializer
from users.models import User


class EducationModuleTestCase(APITestCase):
    """ Тестирование эндпоинтов образовательного модуля. """
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345",
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.edu_module = EducationModule.objects.create(
            title="test_module",
            description="test_description",
        )

    def test_edu_module_create(self):
        """ Тест создания образовательного модуля. """
        data = {
            "title": "some_test_module",
            "description": "some_test_description",
        }

        response = self.client.post("/education/modules/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationModule.objects.all().count(), 2)

    def test_edu_module_get(self):
        """ Тест получения списка всех образовательных модулей. """
        response = self.client.get(
            "/education/modules/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edu_module_patch(self):
        """ Тест изменения данных образовательного модуля. """
        data = {
            "description": "another_test_description",
        }

        response = self.client.patch(f"/education/modules/{self.edu_module.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edu_module_delete(self):
        """ Тест удаления образовательного модуля. """
        response = self.client.delete(f"/education/modules/{self.edu_module.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LessonTestCase(APITestCase):
    """ Тестирование эндпоинтов уроков. """
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345",
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.edu_module = EducationModule.objects.create(
            title="test_module",
            description="test_description",
        )

        self.lesson = Lesson.objects.create(
            module=self.edu_module,
            number=1,
            title="test_lesson",
            description="test_description",
        )

    def test_lesson_create(self):
        """ Тест создания урока. """
        url = reverse("education:lesson_create")
        data = {
            "module": self.edu_module.id,
            "number": "1",
            "title": "some_test_lesson",
            "description": "some_test_description"
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_list(self):
        """ Тест получения списка всех уроков. """
        url = reverse("education:lesson_list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_retrieve(self):
        """ Тест просмотра одного урока. """
        url = reverse("education:lesson_detail", kwargs={"pk": self.lesson.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        """ Тест изменения данных урока. """
        url = reverse("education:lesson_update", kwargs={"pk": self.lesson.id})
        data = {
            "description": "another_test_description",
        }

        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        """ Тест удаления урока. """
        url = reverse("education:lesson_delete", kwargs={"pk": self.lesson.id})

        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class EducationModuleModelTest(TestCase):
    """ Тестирование модели образовательного модуля. """
    def setUp(self) -> None:
        self.edu_module = EducationModule.objects.create(
            title="test_module",
            description="test_description",
        )

    def test_model(self):
        """ Тест корректного заполнения полей модели. """
        self.assertEqual(self.edu_module.title, "test_module")
        self.assertEqual(self.edu_module.description, "test_description")
        self.assertEqual(str(self.edu_module), "test_module")

    def test_verbose_names(self):
        """ Тест корректного заполнения метаданных. """
        self.assertEqual(EducationModule._meta.verbose_name, "Образовательный модуль")
        self.assertEqual(EducationModule._meta.verbose_name_plural, "Образовательные модули")

    def test_ordering(self):
        """ Тест корректного определения сортировки. """
        self.assertEqual(EducationModule._meta.ordering, ("id",))

    def test_field_max_length(self):
        """ Тест корректного присвоения значения в поле модели. """
        name_field = EducationModule._meta.get_field('title')
        self.assertEqual(name_field.max_length, 250)


class LessonModelTest(TestCase):
    """ Тестирование модели урока. """
    def setUp(self) -> None:
        self.edu_module = EducationModule.objects.create(
            title="test_module",
            description="test_description",
        )

        self.lesson = Lesson.objects.create(
            module=self.edu_module,
            number=1,
            title="test_lesson",
            description="test_description",
        )

    def test_model(self):
        """ Тест корректного заполнения полей модели. """
        self.assertEqual(self.lesson.title, "test_lesson")
        self.assertEqual(self.lesson.description, "test_description")
        self.assertEqual(str(f"{self.edu_module.id} - {self.lesson.title}"), f"{self.edu_module.id} - test_lesson")

    def test_verbose_names(self):
        """ Тест корректного заполнения метаданных. """
        self.assertEqual(Lesson._meta.verbose_name, "Урок")
        self.assertEqual(Lesson._meta.verbose_name_plural, "Уроки")

    def test_ordering(self):
        """ Тест корректного определения сортировки. """
        self.assertEqual(Lesson._meta.ordering, ("id",))

    def test_field_max_length(self):
        """ Тест корректного присвоения значения в поле модели. """
        name_field = Lesson._meta.get_field('title')
        self.assertEqual(name_field.max_length, 250)


class EducationModuleSerializerTestCase(TestCase):
    """ Тестирование сериализатора модели - EducationModule. """

    def test_edu_module_serializer(self):
        modul_1 = EducationModule.objects.create(title="test 1", description="test_description_1")
        modul_2 = EducationModule.objects.create(title="test 2", description="test_description_2")
        data = EducationModuleSerializer([modul_1, modul_2], many=True).data
        expected_data = [
            {
                'id': modul_1.id,
                'title': 'test 1',
                'description': "test_description_1"
            },
            {
                'id': modul_2.id,
                'title': 'test 2',
                'description': "test_description_2"
            },
        ]
        self.assertEqual(data, expected_data)


class LessonSerializerTestCase(TestCase):
    """ Тестирование сериализатора модели - Lesson. """
    def setUp(self) -> None:
        self.edu_module = EducationModule.objects.create(
            title="test_module",
            description="test_description",
        )

    def test_lesson_serializer(self):
        lesson_data = {
            "module": self.edu_module.id,
            "number": 1,
            "title": "test_lesson",
            "description": "test_description"
        }

        serializer = LessonSerializer(data=lesson_data)

        self.assertTrue(serializer.is_valid())

        lesson = serializer.save()

        self.assertEqual(lesson.module, self.edu_module)
        self.assertEqual(lesson.number, 1)
        self.assertEqual(lesson.title, "test_lesson")
        self.assertEqual(lesson.description, "test_description")
