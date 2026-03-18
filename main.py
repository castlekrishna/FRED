import modules.operations as operations
def main():
    try:
        while True:
            command = input(">> ").lower()
            if command == "/bye":
                print("Byiee...")
                break
            if "open" in command:
                operations.browser(command)
    except KeyboardInterrupt:
         print("\nByiee...")


if __name__== "__main__":
       main()