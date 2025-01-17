# Use the official Python image from the Docker Hub
FROM python:3.10-slim 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install system dependencies including PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean

# Install the required packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Create the staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DataEngineeringSite.wsgi:application"]
