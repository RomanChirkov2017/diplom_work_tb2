from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView

from education.models import EducationModule, Lesson
from education.pagination import LessonPagination, EducationModulePagination
from education.serializers import EducationModuleSerializer, LessonSerializer


class EducationModuleViewSet(ModelViewSet):
    """ Эндпоинт для модели образовательного модуля. """
    serializer_class = EducationModuleSerializer
    queryset = EducationModule.objects.all()
    pagination_class = EducationModulePagination


class LessonCreateAPIView(CreateAPIView):
    """ Эндпоинт для создания урока. """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """ Эндпоинт для изменения урока. """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(ListAPIView):
    """ Эндпоинт для вывода списка всех уроков. """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    """ Эндпоинт для просмотра одного урока. """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    """ Эндпоинт для удаления урока. """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
