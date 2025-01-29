from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from gemini_utils import query_gemini_model  # Import the new Gemini function

app = FastAPI()

# Enable CORS so the frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Google Gemini API is now integrated!"}

@app.post("/chat")
async def chat(message: dict):
    try:
        user_message = message["message"]
        response = query_gemini_model(user_message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
