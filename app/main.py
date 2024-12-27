from fastapi import FastAPI
from app.routes.document import router
from app.db.connection import engine
from app.db.models.document import Document

# Create tables in the database
Document.metadata.create_all(bind=engine)
app = FastAPI(title="Document Manager", version="1.0.0")

# Register routes
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Manager API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
