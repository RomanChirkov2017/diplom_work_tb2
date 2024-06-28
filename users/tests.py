from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Тестирование эндпоинтов пользователя. """
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345",
            country="Switzerland"
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест создания пользователя."""
        url = reverse("users:register")
        data = {"email": "test_test@yandex.ru", "password": "54321"}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("email"), "test_test@yandex.ru")

    def test_user_list(self):
        """ Тест просмотра списка пользователей. """
        url = reverse("users:user_list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        """ Тест изменения данных пользователя. """
        url = reverse("users:user_update", kwargs={"pk": self.user.id})
        data = {
            "country": "New Zealand",
        }

        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """ Тест удаления пользователя. """
        url = reverse("users:user_delete", kwargs={"pk": self.user.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
