# Use a base image (preferably a slim version to keep the image small)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --retries 3 -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
