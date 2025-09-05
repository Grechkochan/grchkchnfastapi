# FastAPI Q&A Project

## Описание проекта

Это проект API-сервиса для вопросов и ответов, разработанный на FastAPI и PostgreSQL. Сервис позволяет:

- Создавать вопросы
- Добавлять ответы к вопросам
- Получать список всех вопросов и ответов
- Удалять вопросы и ответы

Технологии:
- Python 3.11
- FastAPI
- SQLAlchemy ORM
- Alembic для миграций
- PostgreSQL
- Docker + Docker Compose


## Инструкция по запуску

1. Клонировать репозиторий:

git clone https://github.com/Grechkochan/grchkchnfastapi.git

cd grchkchnfastapi


2. Собрать и запустить контейнеры:

docker compose up --build -d


3. Прогнать миграции для создания таблиц в базе данных:

docker compose exec web alembic upgrade head


4. Проверить, что сервис работает, открыв в браузере:

http://localhost:8000/docs

## Примечание
- Для удаления всех данных базы данных используйте:
docker compose down -v


