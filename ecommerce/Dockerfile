# Use the official Python image as a base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "server.py", "manage.py", "runserver", "0.0.0.0:8000"]
