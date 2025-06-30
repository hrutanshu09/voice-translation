# crypto_utils.py
from cryptography.fernet import Fernet
import re
import os

# Load or generate key
FERNET_KEY = os.getenv("FERNET_KEY") or Fernet.generate_key().decode()
fernet = Fernet(FERNET_KEY.encode())

# Match single 4-digit numbers
FOUR_DIGIT_PATTERN = re.compile(r"\b\d{4}\b")

def encrypt_4digit_numbers(text: str) -> str:
    def encrypt_match(match):
        plaintext = match.group(0)
        encrypted = fernet.encrypt(plaintext.encode()).decode()
        return f"[ENCRYPTED:{encrypted}]"

    return FOUR_DIGIT_PATTERN.sub(encrypt_match, text)
