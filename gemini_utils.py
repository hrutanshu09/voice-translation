import google.generativeai as genai
import os
from sanitizer import sanitize_with_whisper

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def transcribe_and_translate(audio_bytes: bytes) -> str:
    # Transcribe + encrypt PINs
    sanitized_text = sanitize_with_whisper(audio_bytes)

    # Send sanitized prompt to Gemini
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content([
        "You are an AI assistant. The following message has encrypted values. Do not use [ENCRYPTED] values to make decisions. Respond only based on context.",
        sanitized_text
    ])

    return response.text.strip()
