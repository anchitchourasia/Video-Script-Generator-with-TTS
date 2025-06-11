import os
import tempfile
import edge_tts
import asyncio

class TTSEngine:
    def generate_speech(self, text, language="en", voice_id="en-US-JennyNeural"):
        output_path = os.path.join(tempfile.gettempdir(), "output.mp3")
        
        async def run():
            communicate = edge_tts.Communicate(text, voice_id)
            await communicate.save(output_path)

        try:
            asyncio.run(run())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run())

        return output_path
