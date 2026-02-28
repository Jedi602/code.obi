# app/routers/chat.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import ChatRequest, ChatResponse
from app.dependencies import get_current_user
from app.database import get_db
from app.crud import create_message
from app.ai_client import get_ai_response

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, token: str, db: Session = Depends(get_db)):
    # Authenticate user
    user = get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Save user message
    create_message(db, session_id=request.session_id, sender="user", content=request.message)
    
    # Call AI
    ai_text = get_ai_response(request.message)
    
    # Save AI message
    create_message(db, session_id=request.session_id, sender="AI", content=ai_text)
    
    return ChatResponse(message=ai_text)