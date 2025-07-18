
# Use Ubuntu as the base image
FROM python:3.13.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-dev libpq-dev gcc build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python3 manage.py collectstatic --noinput || true


# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "Skillshare.wsgi:application", "--bind", "0.0.0.0:8000"]
