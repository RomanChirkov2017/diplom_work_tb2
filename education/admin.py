from django.contrib import admin

from education.models import EducationModule, Lesson


@admin.register(EducationModule)
class EducationModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description",)
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "module",)
    list_filter = ("number",)
    search_fields = ("title", "module",)

