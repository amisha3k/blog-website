# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && apt-get clean


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files into the container
COPY . .

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Expose port 8000 for the app
EXPOSE 8000

# Command to run the Django app using gunicorn
CMD ["gunicorn", "myproject1.wsgi:application", "--bind", "0.0.0.0:8000"]
