import random
import time
import json
from modules.utils import line

# game
def game(starting_number,ending_number,attempt):
    start_time = time.time()
    computer_number = random.randint(starting_number,ending_number)
    # hint = 2 upgrade
    while True:
        user_input = input(f"Enter a number ({starting_number} ≤ number ≤ {ending_number}) or type 'hint': ")
        line()
        if user_input.lower() == "hint":
            if computer_number % 2 == 0:
                print("Number is even")
                line()
            else:
                print("Number is odd")
                line()
            continue
        try:
            user_input = int(user_input)
            line()
        except:
            print(f"write number in {starting_number} ≤ number ≤ {ending_number} range or type 'hint'")
            line()
        else:
            if user_input == computer_number:
                end_time = time.time()
                print("Yaayyy...You guessed the number right")
                print(f"Attempt taken: {attempt}")
                total_time = round(end_time-start_time,2)
                print(f"Time taken: {total_time} seconds")
                line()
                return total_time,attempt
            elif ending_number < user_input or user_input < starting_number:
                print(f"Bro... atleast write number in {starting_number} ≤ number ≤ {ending_number} range")
                line()
            elif user_input>computer_number:
                print("Lower")
                line()
            elif user_input < computer_number:
                print("Higher")
                line()
            else:
                print("Invalid input...")
                line()
            attempt += 1
            
        
#game options
def gameoptions():
    print("Choose difficulty\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n0. Exit")
    line()
    while True:
        try:
            choice = int(input("Enter index: "))
            line()
        except:
            print("Enter correct choice...")
            line()
            continue
        else:
            while True:
                if choice == 1:
                    return 0,50,"Easy"
                elif choice == 2:
                    return 0,100,"Medium"
                elif choice == 3:
                    return 0,500,"Hard"
                elif choice == 4:
                    try:
                        starting_number = int(input("Enter starting number: "))
                    except:
                        print("Invalid input...!!")
                        line()
                    else:
                        try:
                            ending_number = int(input("Enter ending number: "))
                            line()
                        except:
                            print("Invalid input...!!")
                            line()
                        else:
                            if starting_number > ending_number:
                                print("Ending point is less than starting point.. please enter a valid input..!!")
                                line()
                            else:
                                return starting_number,ending_number,"Custom"
                elif choice == 0:
                    return None
                
# saving history
def save_history(game_type,starting_point,ending_point,attempt,time_taken):
    data = {
        "Game Type" : game_type,
        "Game range" : f"{starting_point}-{ending_point}",
        "Attempt" : attempt,
        "Time Taken" : time_taken
    }
    try:
        with open ("data/games/guess_number.json","r") as f:
            past_data = json.load(f)
    except:
        past_data = []
    past_data.append(data)
    with open("data/games/guess_number.json","w") as f:
        json.dump(past_data,f,indent=4)
#show history
def show_history():
    try:
        with open("data/games/guess_number.json","r") as f:
            data = json.load(f)
            return data
    except:
        return None
#stats
def stats():
    data = show_history()
    if data is None:
        print("Play a game first.")
        line()
    else:
        total_game = len(data)
        attempts = 0
        total_time_taken = 0
        for item in data:
            attempts += item["Attempt"]
            total_time_taken += item["Time Taken"]
        print(f"Total game: {total_game}")
        print(f"Average attempt: {attempts/total_game:.2f}")
        print(f"Average time taken: {total_time_taken/total_game:.2f}")
        line()
#setting
def setting():
    while True:
        try:
            print("1. Clear all game records\n2. User manual\n3. About game\n0. Exit")
            line()
            choice = int(input("Choose index: "))
            line()
        except:
            line()
            print("Choose correct index...")
            line()
        else:
            if choice == 1:
                with open ("history.json","w") as r:
                    print("All data cleared")
                    line()
                    break
            elif choice == 2:
                print("""NUMBER GUESSING GAME — USER MANUAL

                1. Play
                Choose a difficulty level (Easy, Medium, Hard, or Custom).
                The computer will generate a random number within the selected range.
                Enter guesses until you find the correct number.
                The game will tell you whether to guess Higher or Lower.

                2. Stats
                Displays overall statistics including:

                * Total games played
                * Average number of attempts
                * Average time taken

                3. History
                Shows records of previous games including:

                * Game mode
                * Number range
                * Attempts taken
                * Time taken

                4. Settings
                Allows you to manage the game data:

                * Clear all saved game records
                * View information about the game
                * Exit the settings menu

                5. Exit
                Closes the game safely.

                Note:
                Enter numbers only. Invalid inputs will be rejected and you will be asked to try again.
                """)
                line()
            elif choice == 3:
                print("Number Guessing Game built with Python.\nGuess the correct number within a selected range.\nThe game tracks attempts, time taken, and saves history using JSON.")
                line()
            elif choice == 0:
                print("Exiting...")
                line()
                return

#main
def start():
    line()
    print(" "*15,"Number Guessing Game", " "*20)
    line()
    while True:
        print("1. Play\n2. Stats\n3. History\n4. Setting\n0. Exit")
        line()
        try:
            choice = int(input(("Enter Index: ")))
            line()
        except:
            line()
            print("Invalid input...!!")
            line()
        else:
            if choice == 1:
                parameter = gameoptions()
                if parameter is None:
                    print("Exiting...!!")
                    line()
                else:
                    starting_point,ending_point,game_type = parameter
                    game_data = game(starting_point,ending_point,1)
                    total_time,attempt = game_data
                    save_history(game_type,starting_point,ending_point,attempt,total_time)
            elif choice ==2:
                stats()
            elif choice == 3:
                data = show_history()
                if data is None:
                    print("Play a game first...")
                    line()
                else:
                    for item in data:
                        print("Game Type: ", item["Game Type"])
                        print("Game range: ", item["Game range"])
                        print("Attempt: ", item["Attempt"])
                        print("Time Taken: ",item["Time Taken"],"seconds")
                        line()
            elif choice ==4:
                setting()
            elif choice == 0:
                print("Thanks for playing...")
                line()
                break
            else:
                print("Invalid Choice")
                line()