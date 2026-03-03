import json

class DocParser:
    def run(self, doc_path):
        with open(doc_path, "r") as f:
            data = json.load(f)
        return {
            "gear_teeth": data.get("gear_teeth"),
            "bearing_balls": data.get("bearing_balls"),
            "pitch_diameter": data.get("pitch_diameter"),
        }
