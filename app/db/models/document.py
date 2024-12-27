from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text
from app.db.connection import Base
from sqlalchemy.sql import func


class Document(Base):  # Inherit from Base
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    parsed_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())