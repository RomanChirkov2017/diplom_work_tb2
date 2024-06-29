from django.db import models

from users.models import NULLABLE


class EducationModule(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название модуля")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"
        ordering = ("id",)


class Lesson(models.Model):
    module = models.ForeignKey(
        EducationModule, on_delete=models.CASCADE, verbose_name="Образовательный модуль"
    )
    number = models.PositiveIntegerField(verbose_name="Порядковый номер урока")
    title = models.CharField(max_length=250, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(
        upload_to="education/", verbose_name="Изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.module} - {self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("id",)
