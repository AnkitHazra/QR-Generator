# Dockerfile — pins Python 3.11 and installs system deps needed by Pillow
FROM python:3.11.4-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system libraries required for Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libtiff5-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . /app

# Expose port for Render
EXPOSE 10000

# Start server (Render provides $PORT)
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:${PORT:-10000}"]
