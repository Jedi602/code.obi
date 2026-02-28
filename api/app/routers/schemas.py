from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class ChatRequest(BaseModel):
    session_id: int
    message: str

class ChatResponse(BaseModel):
    message: str