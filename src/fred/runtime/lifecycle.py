from .state import LifecycleState


class Lifecycle:
    def __init__(self):
        self.state = LifecycleState.STOPPED

    def start(self):
        self.state = LifecycleState.STARTING
        print("FRED is starting...")

        self.state = LifecycleState.READY
        print("FRED is ready.")

    def shutdown(self):
        self.state = LifecycleState.SHUTTING_DOWN
        print("FRED is shutting down...")

        self.state = LifecycleState.STOPPED
        print("FRED has stopped.")