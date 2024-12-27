from fastapi import FastAPI
from app.routes.routes import router


app = FastAPI(title="Document Manager", version="1.0.0")

# Register routes
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Manager API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
