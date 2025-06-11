import os

def generate_storyboard(script_text: str, out_path="storyboards/storyboard.txt"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)  # ✅ Ensure folder exists

    with open(out_path, 'w') as f:
        f.write(script_text)
    return out_path
