from dataclasses import dataclass
from typing import List
import google.generativeai as genai
import os
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

class ScriptGenerator:
    def __init__(self):
        self.templates = {
            "educational": "Generate an {length} educational video script in {language} on topic '{topic}'. Include hook, scenes, and CTA. Use simple, engaging language.",
            "promotional": "Create a {length} promotional video script in {language} for '{topic}'. Highlight problem, solution, benefits, and CTA.",
            "storytelling": "Tell a {length} story in {language} about '{topic}'. Include setup, conflict, resolution, and moral takeaway."
        }

    def generate_script(self, topic: str, video_type: str, length: str, language: str = "en") -> Script:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = self.templates[video_type].format(topic=topic, length=length, language=language)
        response = model.generate_content(prompt)
        content = response.text

        return Script(
            title=f"{topic.title()} Video",
            hook="",
            scenes=[],
            call_to_action="Like and subscribe for more!",
            content=content
        )
