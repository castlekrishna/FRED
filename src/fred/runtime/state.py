from enum import Enum

class LifecycleState(Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    READY = "ready"
    PROCESSING = "processing"
    SHUTTING_DOWN = "shutting_down"