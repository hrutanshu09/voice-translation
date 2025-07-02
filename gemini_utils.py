import google.generativeai as genai
import os
from sanitizer import transcribe_with_whisper
from crypto_utils import encrypt_4digit_numbers

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def process_audio(audio_bytes: bytes) -> str:
    # Step 2: Transcribe bytes to text
    transcript = transcribe_with_whisper(audio_bytes)

    # Step 3: Encrypt sensitive values
    sanitized_text = encrypt_4digit_numbers(transcript)

    # Step 4: Send sanitized prompt to Gemini
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content([
        "You are an AI assistant. Ignore [ENCRYPTED] data. Translated and sanitized message follows:",
        sanitized_text
    ])
    return response.text.strip()
