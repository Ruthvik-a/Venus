from g4f.client import ClientFactory, Client
from memory import get_history, add_message

# ===== AI MODELS CONFIG =====
AI_MODELS = {
    "default": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"
    },
    "gemini": {
        "provider": "gemini",
        "model": "models/gemini-2.5-flash"
    },
    "oss": {
        "provider": "groq",
        "model": "openai/gpt-oss-120b"
    }
}

# ===== CHAT AI =====
def chat_ai(prompt: str, session_id="default", ai_name="default"):
    
    model_info = AI_MODELS.get(ai_name, AI_MODELS["default"])

    history = get_history(session_id)
    history.append({"role": "user", "content": prompt})

    try:
        client = ClientFactory.create_client(model_info["provider"])

        response = client.chat.completions.create(
            model=model_info["model"],
            messages=history,
        )

        reply = response.choices[0].message.content

        add_message(session_id, "assistant", reply)

        return reply  # ✅ ONLY AI RESPONSE

    except Exception:
        return "HextorAI is busy. Try again later."


# ===== IMAGE GENERATION =====
def generate_image(prompt: str):
    try:
        client = Client()

        response = client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )

        return response.data[0].url  # ✅ ONLY IMAGE URL

    except Exception:
        return "Image generation failed"
