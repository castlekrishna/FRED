from .environment import Environment
from .lifecycle import Lifecycle
from ..config.directories import DataDirectoryManager
from ..config.manager import ConfigManager


class Bootstrap:
    def __init__(self):
        self.environment = None
        self.directories = None
        self.config = None
        self.lifecycle = None

    def initialize(self):
        print("Initializing FRED...")

        self.environment = Environment()

        data_directory = self.environment.get_data_directory()

        self.directories = DataDirectoryManager(data_directory)
        self.directories.initialize()

        self.config = ConfigManager(self.directories)
        self.config.load()

        self.lifecycle = Lifecycle()

        print("FRED initialization complete.")

    def start(self):
        self.lifecycle.start()

    def shutdown(self):
        self.lifecycle.shutdown()