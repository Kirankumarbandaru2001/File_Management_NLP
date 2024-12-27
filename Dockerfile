# Use a lightweight Python image
FROM python:3.10-slim

# Set environment variables for consistent builds
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file into the container for dependency installation
COPY requirements.txt .

# Install dependencies with pip
RUN pip install --no-cache-dir --retries 3 -r requirements.txt

# Copy the entire backend `app` directory into the container
COPY app ./app

# Copy Alembic configuration files for database migrations
COPY alembic.ini .
COPY alembic ./alembic

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
