
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from g4f.client import Client

app = FastAPI()
client = Client()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    message = data.get("message","")
    model = data.get("model","gpt-4o-mini")
    provider = data.get("provider", None)

    kwargs = {}
    if provider:
        kwargs["provider"] = provider

    response = client.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":message}],
        **kwargs
    )
    return {"reply": response.choices[0].message.content}
