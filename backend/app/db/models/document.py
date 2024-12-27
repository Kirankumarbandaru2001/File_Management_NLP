from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from app.db.connection import Base
from sqlalchemy.sql import func

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    parsed_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())


    








