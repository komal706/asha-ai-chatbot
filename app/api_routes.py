from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Correct CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Explicitly allow OPTIONS
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")

    if not query:
        return JSONResponse({"error": "Query is required"}, status_code=400)

    try:
        response_text = f"Here are some job opportunities in Bangalore for women: Example1, Example2, Example3."
        return {"response": response_text}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
