# app/schemas.py

from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    session_id: str
    query: str

class ChatResponse(BaseModel):
    answer: str
