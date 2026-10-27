from pathlib import Path


class DataDirectoryManager:
    def __init__(self, base_directory):
        self.base_directory = Path(base_directory)

    def initialize(self):
        directories = [
            "config",
            "memory",
            "preferences",
            "habits",
            "history",
            "logs",
            "cache",
        ]

        for directory in directories:
            path = self.base_directory / directory
            path.mkdir(parents=True, exist_ok=True)

    def get_directory(self, name):
        return self.base_directory / name