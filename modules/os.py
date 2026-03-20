import subprocess

def open_vscode():
    print("Opening VS Code")
    subprocess.Popen(["code", "--new-window", "/home/krishu/Fred/"])
def open_clock():
    print("Opening Clock")
    subprocess.Popen(["gnome-clocks"])