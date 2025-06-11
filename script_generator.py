import os
import google.generativeai as genai
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@dataclass
class Scene:
    content: str
    description: str
    visuals: List[str]
    duration: float

@dataclass
class Script:
    title: str
    hook: str
    scenes: List[Scene]
    call_to_action: str
    content: str

    def export(self, filename: str):
        with open(filename, 'w') as f:
            f.write(self.content)

class ScriptGenerator:
    def __init__(self):
        self.templates = {
            "educational": {"hook": "Did you know that {topic} can change your life?"},
            "promotional": {"hook": "Tired of {topic}? Discover the solution!"},
            "storytelling": {"hook": "Let me tell you an amazing story about {topic}"},
        }

    def generate_script(self, topic: str, video_type: str, length: str, language: str) -> Script:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        Generate a detailed {video_type} video script in **{language}** on the topic: {topic}.
        Make it {length} in length. Include a hook, structured scenes, and a clear call-to-action.
        The entire response should be in **{language}** and easy to understand.
        """
        response = model.generate_content(prompt)
        script_text = response.text

        return Script(
            title=f"Video about {topic}",
            hook=self.templates[video_type]["hook"].format(topic=topic),
            scenes=[],
            call_to_action="Like and subscribe for more content!",
            content=script_text
        )
