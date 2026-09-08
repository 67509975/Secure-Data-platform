from fastapi import FastAPI

from app.core.config import settings
from app.database.database import Base, engine
from app.models.user import User
from app.api.routes.users import router as users_router
from app.api.routes.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(users_router)
app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }