# Document Manager API

## Overview
This project allows users to upload, store, and manage documents. It supports multiple file formats and uses AWS S3 for file storage.


## Features
- Upload documents to AWS S3.
- Store metadata in PostgreSQL.
- Validate file type and size.
- Dockerized for deployment.


## Setup Instructions
1. Clone the repository:

2. Add your `.env` file with the necessary environment variables.
3. Build and run the application:
docker-compose up --build

4. Access the API at `http://localhost:8000`.

## Endpoints
- `POST /api/documents`: Upload a document.

## Future Enhancements
- Add NLP processing and RAG agent integration.
- Implement user authentication.
- Add frontend for better usability.

