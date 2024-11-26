FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем кодировку
ENV PYTHONIOENCODING=utf-8

# Запускаем приложение
CMD ["python", "main.py"]
