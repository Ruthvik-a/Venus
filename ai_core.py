from g4f.client import ClientFactory, Client

# =========================
# MODEL CONFIG (HIDDEN FROM USER)
# =========================
MODELS = {
    "default": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"
    },
    "oss": {
        "provider": "groq",
        "model": "openai/gpt-oss-120b"
    },
    "gemini": {
        "provider": "gemini",
        "model": "models/gemini-2.5-flash"
    }
}

# =========================
# CHAT AI FUNCTION
# =========================
def chat_ai(prompt: str, model_choice: str = "default"):
    try:
        config = MODELS.get(model_choice, MODELS["default"])

        client = ClientFactory.create_client(config["provider"])

        response = client.chat.completions.create(
            model=config["model"],
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        # fallback to default model if error
        try:
            config = MODELS["default"]
            client = ClientFactory.create_client(config["provider"])
            response = client.chat.completions.create(
                model=config["model"],
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content.strip()
        except:
            return "HextorAI is busy. Try again later."


# =========================
# IMAGE AI FUNCTION
# =========================
def image_ai(prompt: str):
    try:
        client = Client()
        response = client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )
        return response.data[0].url
    except Exception:
        return "HextorAI image engine is busy."
