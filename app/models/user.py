from sqlalchemy import Boolean, Column , Column , Integer, String
from app.database.database import Base

class User(Base):
    __tablename__= "users"
    id =Column(Integer, primary_key=True, index=True)
    username = Column(String(50),unique=True, nullable=False, index=True)
    email = Column(String(255),unique=True, nullable=False, index=True)
    hashed_password =Column(String(255),nullable=False)
    role =Column(String(20),nullable=False, default="user")
    is_active=Column(Boolean, nullable=False,default=True)