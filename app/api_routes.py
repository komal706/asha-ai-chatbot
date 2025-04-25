from fastapi import APIRouter, Request
from app.chat_engine import generate_response

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = generate_response(user_input)
    return {"response": response}
