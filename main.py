import modules.operations as operations
from modules.games.guess_number import start
from modules.chat import reply

def main():
    try:
        while True:
            command = input(">> ").lower()
            if command == "/bye":
                print("Byiee...")
                break
            if "open" in command:
                operations.browser(command)
            if "play" in command:
                 operations.handle_play(command)
            responce = reply(command)
            if responce:
                 print(responce)
            if "time" in command:
                 operations.show_time()
            if "status" in command:
                operations.show_projects(command)
            if "working" in command:
                 operations.add_feature(command)
            if "study" in command:
                 operations.study()
    except KeyboardInterrupt:
         print("\nByiee...")


if __name__== "__main__":
       main()