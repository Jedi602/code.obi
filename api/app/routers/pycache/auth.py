# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from passlib.hash import bcrypt

from app.schemas import UserCreate
from app.database import get_db
from app.models import User
from app.config import SECRET_KEY

router = APIRouter()

JWT_EXPIRATION_MINUTES = 60 * 24  # 1 day

# Helper: create JWT token
def create_access_token(user_id: int):
    payload = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = bcrypt.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = create_access_token(new_user.id)
    return {"access_token": token, "user_id": new_user.id}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not bcrypt.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(db_user.id)
    return {"access_token": token, "user_id": db_user.id}