# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
def get_profile(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }

@router.get("/subscription")
def get_subscription(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Placeholder for subscription plan
    plan = getattr(user, "subscription_plan", "free")
    return {"plan": plan}