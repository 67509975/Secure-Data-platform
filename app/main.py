from fastapi import FastAPI
from app.core.config import settings
from app.database.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment
    }