import json
from .defaults import DEFAULT_CONFIG

class ConfigManager:
    def __init__(self, directory_manager):
        self.directory_manager = directory_manager
        self.path = self.directory_manager.get_directory("config") / "config.json"
        self.config = {}

    def load(self):
        if not self.path.exists():
            self.config = DEFAULT_CONFIG.copy()
            self.save()
            return

        with self.path.open("r", encoding="utf-8") as file:
            self.config = json.load(file)

        if not self.validate():
            raise ValueError("Invalid FRED configuration")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

    def delete(self, key):
        if key in self.config:
            del self.config[key]
            self.save()

    def validate(self):
        if not isinstance(self.config.get("fred_version"), str):
            return False

        if not isinstance(self.config.get("interface"), str):
            return False

        if not isinstance(self.config.get("logging"), bool):
            return False

        return True

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4)