#!/bin/bash

# Step 1: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 2: Collect static files (necessary for production)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 3: Apply migrations (in case any migrations are pending)
echo "Applying migrations..."
python manage.py migrate

# Step 4: Start the application using Gunicorn
echo "Starting application with Gunicorn..."
gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
