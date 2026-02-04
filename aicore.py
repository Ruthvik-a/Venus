from g4f.client import ClientFactory, Client
from config import MODELS, FALLBACKS
from memory import get_history, add_message

image_client = Client()

def auto_mode(prompt: str):
    prompt_lower = prompt.lower()

    if len(prompt) < 20:
        return "FAST"
    if "code" in prompt_lower or "algorithm" in prompt_lower or "logic" in prompt_lower:
        return "SMART"
    if "story" in prompt_lower or "creative" in prompt_lower:
        return "GEMINI"
    if len(prompt) > 200:
        return "ULTRA"

    return "FAST"


def chat_ai(prompt: str, session_id="default", mode="AUTO"):
    if mode == "AUTO":
        mode = auto_mode(prompt)

    model_data = MODELS.get(mode, MODELS["FAST"])

    history = get_history(session_id)
    history.append({"role": "user", "content": prompt})

    try:
        client = ClientFactory.create_client(model_data["provider"])
        response = client.chat.completions.create(
            model=model_data["model"],
            messages=history,
        )
        reply = response.choices[0].message.content
        add_message(session_id, "assistant", reply)
        return reply, mode

    except Exception:
        for provider, model in FALLBACKS:
            try:
                client = ClientFactory.create_client(provider)
                response = client.chat.completions.create(
                    model=model,
                    messages=history,
                )
                reply = response.choices[0].message.content
                add_message(session_id, "assistant", reply)
                return reply, "FALLBACK"
            except:
                continue

    return "⚠️ HextorAI is busy. Try again later.", "ERROR"


def image_ai(prompt: str):
    try:
        response = image_client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )
        return response.data[0].url
    except:
        return None
