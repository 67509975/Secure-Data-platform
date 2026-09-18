from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user , get_users


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user_data)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user