
# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-dev libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /Skillshare

# Install Python dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt gunicorn

# Copy project
COPY . .

# Collect static files
RUN python3 manage.py collectstatic --noinput || true


# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "Skillshare.wsgi:application", "--bind", "0.0.0.0:8000"]
