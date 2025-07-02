import re
from cryptography.fernet import Fernet
import whisper

# Generate this once and store it securely (e.g. in Vault or .env)
FERNET_KEY = Fernet.generate_key()
cipher = Fernet(FERNET_KEY)

def encrypt_sensitive_info(text: str) -> str:
    def encrypt(match):
        token = match.group(0)
        encrypted = cipher.encrypt(token.encode()).decode()
        return f"[ENCRYPTED:{encrypted[:6]}...]"
    return re.sub(r'\b\d{4}\b', encrypt, text)

def sanitize_with_whisper(audio_bytes: bytes) -> str:
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_bytes)

    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.mp3", language="hi")  # use "auto" for auto-detect
    transcript = result["text"]
    return encrypt_sensitive_info(transcript)
