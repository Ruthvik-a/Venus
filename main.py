    from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_core import chat_ai, image_ai

app = FastAPI(title="HextorAI")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "HextorAI online"}

# =========================
# CHAT API
# =========================
@app.post("/chat")
async def chat(data: dict):
    prompt = data.get("prompt", "")
    model = data.get("model", "default")

    if not prompt:
        return {"response": ""}

    answer = chat_ai(prompt, model)
    return {"response": answer}


# =========================
# IMAGE API
# =========================
@app.post("/image")
async def image(data: dict):
    prompt = data.get("prompt", "")

    if not prompt:
        return {"url": ""}

    img_url = image_ai(prompt)
    return {"url": img_url}
