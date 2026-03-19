import modules.router as router




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

