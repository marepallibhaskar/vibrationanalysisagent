import json
import os

class MemoryStore:
    def __init__(self, store_path="memory_store.json"):
        self.store_path = store_path
        self.long_term = self._load_store()

    def _load_store(self):
        if os.path.exists(self.store_path):
            with open(self.store_path, "r") as f:
                return json.load(f)
        return []

    def _save_store(self):
        with open(self.store_path, "w") as f:
            json.dump(self.long_term, f, indent=2)

    def log(self, record):
        self.long_term.append(record)
        self._save_store()

    def query(self, query):
        if "last" in query.lower():
            import re
            match = re.search(r"last (\d+)", query.lower())
            if match:
                n = int(match.group(1))
                return self.long_term[-n:]
        elif "trend" in query.lower():
            faults = [r["fault"] for r in self.long_term]
            return f"Trend: {faults}"
        else:
            return self.long_term
