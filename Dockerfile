# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies specified in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose ports for the Flask app and Prometheus metrics
EXPOSE 8787
EXPOSE 9095

# Set the entry point for the container to run the Flask app
CMD ["python", "scraper_service.py"]
