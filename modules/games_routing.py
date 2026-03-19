
from modules.games.guess_number import start as guess
games_func = {
        "guess" : guess
        
}

def games(command):
        for key,func in games_func.items():
                if key in command:
                        func()
                        return
        print("Command not found")
        print("""Use "play guess" """)