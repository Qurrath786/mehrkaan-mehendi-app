from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db   # ✅ use database.py, not app.db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.utils.security import hash_password   # ✅ moved hashing to utils

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user with hashed password
    user = User(
        name=user_in.name,
        email=user_in.email,
        password=hash_password(user_in.password)  # 🔒 secure
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user   # Pydantic UserRead will exclude password automatically

@router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
