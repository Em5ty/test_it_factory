# API для учета посещений торговых точек

Это простое API на Django, предназначенное для регистрации посещений сотрудников торговых точек.

## Установка и Запуск в Docker

1. Убедитесь, что у вас установлен Docker на вашей машине.

2. Склонируйте репозиторий:

```bash
git clone https://github.com/Em5ty/test_it_factory
cd store_visit
```

Запустите приложение с помощью Docker Compose:

```bash
docker-compose up --build
```

    Примените миграции:

```bash
docker-compose run web python manage.py migrate
```

    Создайте суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

API будет доступно по адресу http://localhost:8000/.

Использование

    После запуска проекта, вы можете зайти в админку Django, чтобы создать и редактировать записи о сотрудниках, торговых точках и посещениях. Админка доступна по адресу http://localhost:8000/admin/.

    Для доступа к API используйте следующие эндпоинты, как описано в предыдущем README.md.

Зависимости

    Docker
    Docker Compose
    Python 3.8+
    Django 2.2+
    Django Rest Framework
    PostgreSQL
