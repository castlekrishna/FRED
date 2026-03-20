
from modules.games.guess_number import start as guess
import modules.help as help
games_func = {
        "guess" : guess
        
}

def games(command):
        for key,func in games_func.items():
                if key in command:
                        func()
                        return
        help.help_games()