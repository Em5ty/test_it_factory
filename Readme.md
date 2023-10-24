# API для учета посещений торговых точек

Это простое API на Django, предназначенное для регистрации посещений сотрудников торговых точек.

## Установка и Запуск в Docker

1. Убедитесь, что у вас установлен Docker на вашей машине.

2. Склонируйте репозиторий:

```bash
git clone <URL-вашего-репозитория>
cd your-project-directory


    Запустите приложение с помощью Docker Compose:

bash

docker-compose up --build

    Примените миграции:

bash

docker-compose run web python manage.py migrate

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