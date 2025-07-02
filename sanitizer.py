import whisper

def transcribe_with_whisper(audio_bytes: bytes) -> str:
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_bytes)

    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.mp3", language="hi")  # or "auto"
    return result["text"]
