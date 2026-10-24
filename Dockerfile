
# Базовий образ Python
FROM python:3.12-slim

# Робоча директорія
WORKDIR /app

# Копіювання файлу залежностей
COPY requirements.txt .

# Встановлення бібліотек
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання вебзастосунку
COPY views.py .

# Порт застосунку
EXPOSE 8080

# Запуск Flask-сервера
CMD ["python", "views.py"]
