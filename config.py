APP_NAME = "HextorAI"

DEFAULT_MODE = "AUTO"

MODELS = {
    "FAST": {
        "provider": "groq",
        "model": "llama-3.1-8b-instant"
    },
    "SMART": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"
    },
    "GEMINI": {
        "provider": "gemini",
        "model": "models/gemini-1.5-flash"
    },
    "ULTRA": {
        "provider": "openai",
        "model": "gpt-4o-mini"
    }
}

FALLBACKS = [
    ("groq", "llama-3.1-8b-instant"),
    ("openai", "gpt-4o-mini"),
]

PUBLIC_API_KEY = "hextor-key-123"
