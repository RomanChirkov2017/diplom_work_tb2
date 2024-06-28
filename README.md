# Django-приложение "Образовательные модули"

### Описание:<br> 
#### Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть: 
- порядковый номер
- название
- описание

### Задача:<br>
#### При создании проекта нужно: 
- реализовать для модели (моделей) все методы CRUD
- полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

### Требуемый стэк: 
- Python 3.11
- Docker
- Django
- DRF
- PostgreSQL
- Git
- Swagger
- PEP8

## Для тестирования в проекте используется UnitTest, для подсчета покрытия используется Coverage.

### Для запуска введите в терминале следующие команды: 
- python manage.py test
- coverage run --source'.' manage.py test
- coverage report

## Документация проекта:

               "http://127.0.0.1:8000/swagger/"

## Для запуска приложения:
* скопируйте данный репозиторий на локальный компьютер;
* создайте и заполните файл .env по шаблону из файла .env.sample;
* выполните команду  docker-compose up -d --build  в терминале.