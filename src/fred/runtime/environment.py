import os
import platform
from pathlib import Path


class Environment:
    def __init__(self):
        self.os = platform.system()
        self.python_version = platform.python_version()
        self.fred_version = "A1.0"

    def get_data_directory(self):
        if self.os == "Windows":
            base_directory = os.getenv("APPDATA")
            return Path(base_directory) / "FRED"

        if self.os == "Darwin":
            return Path.home() / "Library" / "Application Support" / "FRED"

        if self.os == "Linux":
            base_directory = os.getenv("XDG_DATA_HOME")

            if base_directory:
                return Path(base_directory) / "FRED"

            return Path.home() / ".local" / "share" / "FRED"

        raise RuntimeError(f"Unsupported operating system: {self.os}")

    def describe(self):
        return {
            "os": self.os,
            "python_version": self.python_version,
            "fred_version": self.fred_version,
        }