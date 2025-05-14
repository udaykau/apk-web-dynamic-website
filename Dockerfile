# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Ensure static and media directories exist
RUN mkdir -p /app/assets /app/media

# Make and apply migrations, then collect static files
RUN python manage.py makemigrations && python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port (default Django port)
EXPOSE 8000

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
