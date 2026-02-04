from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_core import chat_ai, image_ai
from config import APP_NAME, PUBLIC_API_KEY
import uuid

app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def check_key(key):
    return key == PUBLIC_API_KEY


class ChatRequest(BaseModel):
    message: str
    mode: str | None = "AUTO"
    session_id: str | None = None


class ImageRequest(BaseModel):
    prompt: str


@app.post("/api/chat")
def chat(req: ChatRequest, x_api_key: str = Header(None)):
    if not check_key(x_api_key):
        return {"error": "Invalid API key"}

    session_id = req.session_id or str(uuid.uuid4())

    reply, mode_used = chat_ai(req.message, session_id, req.mode)

    return {
        "ai": "HextorAI",
        "session_id": session_id,
        "mode": mode_used,
        "reply": reply
    }


@app.post("/api/image")
def image(req: ImageRequest, x_api_key: str = Header(None)):
    if not check_key(x_api_key):
        return {"error": "Invalid API key"}

    img = image_ai(req.prompt)

    if not img:
        return {"error": "Image generation failed"}

    return {
        "ai": "HextorAI",
        "image": img
    }


@app.get("/")
def home():
    return {"name": APP_NAME, "status": "online"}
