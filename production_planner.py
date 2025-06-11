import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ProductionPlan:
    scenes: List[Dict]
    total_duration: float

    def export(self, filename: str):
        with open(filename, 'w') as f:
            json.dump({
                "scenes": self.scenes,
                "total_duration": self.total_duration
            }, f, indent=2)

class ProductionPlanner:
    def create_plan(self, script, audio_file: str) -> ProductionPlan:
        return ProductionPlan(
            scenes=[{
                "timestamp": "00:00",
                "content": "Scene 1",
                "description": "Opening shot",
                "visuals": ["Wide angle city view"],
                "duration": 5.0
            }],
            total_duration=5.0
        )
