from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import DATABASE_URL  # This imports the database URL from your settings

# Create the database engine
engine = create_engine(DATABASE_URL)

# Session maker for handling database connections
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = sessionLocal()  # Creates a new session
    try:
        yield db  # Provides the session to the route handler
    finally:
        db.close()  # Closes the session after the request is processed
