import os

def generate_storyboard(script_text: str, out_path: str = "storyboards/storyboard.txt") -> str:
    os.makedirs("storyboards", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        lines = script_text.splitlines()
        for i, line in enumerate(lines):
            if line.strip():
                f.write(f"Scene {i+1}: {line.strip()}\n")
    return out_path

def get_sound_effects_list():
    return [
        "applause", "laugh", "whoosh", "dramatic hit", 
        "swoosh", "typing", "click", "beep"
    ]
