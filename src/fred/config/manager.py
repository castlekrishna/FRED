import json
from pathlib import Path


class ConfigManager:
    def __init__(self, path):
        self.path = Path(path)
        self.config = {}

    def load(self):
        if not self.path.exists():
            self.config = {}
            return

        with self.path.open("r", encoding="utf-8") as file:
            self.config = json.load(file)

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4)