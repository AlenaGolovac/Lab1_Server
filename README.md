
# Lab1_Server

Лабораторна робота №1 з дисципліни
«Технології розроблення серверних компонентів».

## Опис

Вебзастосунок на Python із використанням Flask.
Реалізовано Healthcheck API, контейнеризацію
через Docker Compose та CI через GitHub Actions.

## Технології

- Python 3.12
- Flask 3.1.1
- Docker
- Docker Compose
- GitHub Actions
- Ruff

## Запуск через Docker Compose

1. Запустити Docker Desktop.
2. Відкрити термінал у папці проєкту.
3. Виконати команду:

```bash
docker compose up --build -d
```

## Перевірка роботи

Liveness:
http://127.0.0.1:8080/healthz/live

Readiness:
http://127.0.0.1:8080/healthz/ready

## Перевірка стану контейнера

```bash
docker compose ps
```

## Зупинка контейнера

```bash
docker compose down
```

## Локальний запуск без Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python views.py
```

## CI

GitHub Actions автоматично перевіряє
Python-код за допомогою Ruff,
збирає Docker-образ та перевіряє
конфігурацію Docker Compose.
