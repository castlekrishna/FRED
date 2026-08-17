from .environment import Environment
from .lifecycle import Lifecycle

class Bootstrap:
    def __init__(self):
        self.environment = None
        self.lifecycle = None

    def initialize(self):
        print("Initializing FRED...")

        self.environment = Environment()
        self.lifecycle = Lifecycle()

        print("FRED initialization complete.")

    def start(self):
        self.lifecycle.start()

    def shutdown(self):
        self.lifecycle.shutdown()