from rest_framework import serializers

from education.models import EducationModule, Lesson


class EducationModuleSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели образовательного модуля. """
    class Meta:
        model = EducationModule
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели урока. """
    class Meta:
        model = Lesson
        fields = "__all__"
