import os
from dotenv import load_dotenv


load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = "postgresql://doc_user:doc_password@localhost/document_manager"
