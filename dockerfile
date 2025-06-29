# # Base image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app

# # Install system-level dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     libglib2.0-0 \
#     libsm6 \
#     libxrender1 \
#     libxext6 \
#     libjpeg-dev \
#     zlib1g-dev \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy project files
# COPY . /app

# # Install Python dependencies
# COPY requirements.txt /app/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Expose Django's default port
# EXPOSE 8000

# # Apply database migrations (SQLite trong development)
# RUN python manage.py migrate || true

# # Start Django dev server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ========================================================

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libjpeg-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py migrate || true

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
