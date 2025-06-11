from typing import List, Dict

def create_production_plan(script_text: str) -> List[Dict]:
    """
    Parses script content to produce a structured production plan.
    Assumes script is divided into scenes with scene titles and timing comments.

    Returns:
        List of dictionaries with:
            - timestamp
            - scene title
            - description (narration)
            - visuals (inferred if mentioned in script)
            - duration estimate
    """
    plan = []
    lines = script_text.splitlines()
    current_scene = {}
    visuals = []

    for line in lines:
        line = line.strip()

        if line.startswith("[Scene"):
            if current_scene:
                plan.append(current_scene)
            # Extract timestamp and title
            parts = line.strip("[]").split(" - ")
            scene_info = parts[0].replace("Scene", "").strip()
            title = parts[0].split(":")[1].strip() if ":" in parts[0] else parts[0].strip()
            timestamp = parts[1] if len(parts) > 1 else "0:00"

            current_scene = {
                "timestamp": timestamp,
                "content": f"Scene {scene_info}",
                "description": title,
                "visuals": [],
                "duration": estimate_duration(timestamp)
            }
        elif line.startswith("(Visual:"):
            visuals_line = line.replace("(Visual:", "").replace(")", "").strip()
            visuals = [v.strip() for v in visuals_line.split(",")]
            current_scene["visuals"] = visuals
        elif line and not line.startswith("("):
            # Assume narration
            current_scene.setdefault("description", "")
            current_scene["description"] += " " + line.strip()

    if current_scene:
        plan.append(current_scene)

    return plan

def estimate_duration(timestamp_range: str) -> int:
    """
    Estimate duration from timestamp range like '0:15-0:45'
    """
    try:
        start, end = timestamp_range.split("-")
        def to_seconds(t):
            parts = t.strip().split(":")
            return int(parts[0]) * 60 + int(parts[1])
        return to_seconds(end) - to_seconds(start)
    except Exception:
        return 15  # default fallback
