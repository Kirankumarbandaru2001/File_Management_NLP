from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import DATABASE_URL

# DATABASE_URL = "postgresql://doc_user:doc_password@localhost/document_manager"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Session maker for handling databse connections
sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependecny to get a databse session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        





