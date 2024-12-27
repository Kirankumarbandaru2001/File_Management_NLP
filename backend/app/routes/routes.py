import boto3
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.db.connection import get_db
from app.db.models.document import Document
from app.config.settings import S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

router = APIRouter()

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@router.post("/documents")
async def create_document(title:str,file: UploadFile=File(...),db:Session=Depends(get_db)):
    try:
        # Validate file size
        file_content = await file.read()
        max_file_size = 10*1024*1024 # 10 MB
        if len(file_content)>max_file_size:
            raise HTTPException(status_code=400, detail="File size exceeds the 10 MB limit.")
        
        # Validate content type
        supported_types = {"application/pdf", "text/csv", "application/vnd.ms-powerpoint"}
        if file.content_type not in supported_types:
            raise HTTPException(status_code=400, detail="Unsupported dile type.")
        

        # Save the document to AWS S3
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=file.filename, Body=file_content)

        # Store metadata in the database
        document = Document(title=title,file_path=f"s3://{S3_BUCKET_NAME}/{file.filename}",file_type=file.content_type)
        db.add(document)
        db.commit()
        db.refresh(document)
        
        return {"id":document.id,"message":"Document created sucesfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occured: {str(e)}")
