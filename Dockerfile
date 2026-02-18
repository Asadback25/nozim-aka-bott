# Pythonning eng so'nggi barqaror versiyasidan foydalanamiz
FROM python:3.11-slim

# Terminalda loglarni ko'rib turish uchun muhit o'zgaruvchilari
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ishchi katalogni yaratamiz
WORKDIR /app

# Tizim paketlarini yangilaymiz (masalan, PostgreSQL uchun kutubxonalar)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Kutubxonalar ro'yxatini nusxalaymiz va o'rnatamiz
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyihaning qolgan qismini nusxalaymiz
COPY . /app/