# Use an official Python runtime as a parent image, based on Alpine
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Update the package list and install build dependencies
RUN apk add --no-cache --update \
    build-base \
    gcc \
    libffi-dev \
    musl-dev \
    linux-headers \
    openssl-dev \
    curl \
    && pip install --upgrade pip

# Install Flask and Boto3 directly
RUN pip install --no-cache-dir Flask boto3 python-dotenv

# Remove build dependencies to reduce image size
RUN apk del build-base gcc libffi-dev musl-dev linux-headers openssl-dev

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["python3", "-m" ,"flask", "run", "--host=0.0.0.0"]