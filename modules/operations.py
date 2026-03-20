import modules.router as router
import modules.help as help
from datetime import datetime
import modules.memory as memory
import modules.utils as utils
import modules.web as web
import modules.os as os


# opening websites
def browser(command):
    for key,func in router.browsing.items():
                if key in command:
                        func()
                        return
    print("Command not found...")

def handle_play(command):
    for key , func in router.play_map.items():
        if key in command:
            func(command)
    help.help_play()

def show_time():
      now = datetime.now()
      print(now.strftime("%I:%M:%S %p | %d-%m-%y"))
    
def show_projects(command):
    words = command.split()
    project = words[0]
    records = memory.load_project_memory()
    formatted = memory.format_records(project=project,records=records)
    utils.line()
    print(formatted)
    utils.line()

def add_feature(command):
    if "on" and "in" in command:
          text = command.split("on",1)[1].strip()
          feature, project = text.split("in")
          feature = feature.strip()
          project = project.strip()
          memory.update_current_feature(project=project,feature=feature)

def study():
    os.open_vscode()
    web.open_chatgpt()
    web.open_youtube()
    os.open_clock()