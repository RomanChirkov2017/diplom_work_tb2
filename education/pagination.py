from rest_framework.pagination import PageNumberPagination


class EducationModulePagination(PageNumberPagination):
    """ Настройки пагинации для модели образовательного модуля. """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class LessonPagination(PageNumberPagination):
    """ Настройки пагинации для модели урока. """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
