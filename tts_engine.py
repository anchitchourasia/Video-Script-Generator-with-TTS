import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

class TTSEngine:
    def __init__(self):
        self.voice_id = "EXAVITQu4vr4xnSDxMaL"  # Jenny - default ElevenLabs voice

    def generate_speech(self, text: str, language: str = "en", voice_id: str = None) -> str:
        voice_id = voice_id or self.voice_id
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": ELEVEN_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            raise Exception(f"TTS failed: {response.text}")
        out_path = "audio.mp3"
        with open(out_path, "wb") as f:
            f.write(response.content)
        return out_path
