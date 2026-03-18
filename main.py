import modules.operations as operations
from modules.games.guess_number import start
def main():
    try:
        while True:
            command = input(">> ").lower()
            if command == "/bye":
                print("Byiee...")
                break
            if "open" in command:
                operations.browser(command)
            if "guess" in command:
                 start()
    except KeyboardInterrupt:
         print("\nByiee...")


if __name__== "__main__":
       main()