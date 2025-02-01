
# Use the official Python image from the Docker Hub
FROM python:3.9-slim


# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 4520

# Copy the rest of the application code to the container
COPY . .


# Set the entrypoint for the container  
CMD ["python", "app/main.py"]