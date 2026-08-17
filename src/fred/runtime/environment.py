import platform

class Environment:
    def __init__(self):
        self.os = platform.system()
        self.python_version = platform.python_version()
        self.fred_version = "A1.0"

    def describe(self):
        return{
            "os": self.os,
            "python_version" : self.python_version,
            "fred_version" : self.fred_version,
        }