FROM python:3.12-slim

WORKDIR /app

RUN pip install eventlet

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .