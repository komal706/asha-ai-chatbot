# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QueryRequest(BaseModel):
    query: str

# Chat endpoint
@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    response = ollama.chat(
        model="llama3",  # make sure you have llama3 model downloaded
        messages=[{"role": "user", "content": request.query}]
    )
    answer = response['message']['content']
    return {"response": answer}
