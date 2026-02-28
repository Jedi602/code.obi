from fastapi import FastAPI
from app.routers import auth, chat, user

app = FastAPI(title="AI SaaS Backend")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(user.router, prefix="/user", tags=["user"])