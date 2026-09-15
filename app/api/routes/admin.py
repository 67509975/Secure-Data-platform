from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import require_admin
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserResponse


router = APIRouter(
    prefix="/admin",
    tags=["Administration"],
)


@router.get(
    "/users",
    response_model=list[UserResponse],
)
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_admin),
):
    return db.query(User).all()