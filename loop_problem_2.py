import random
import time

# Defining functions

def invalid_option():
    print("\nThat's not a valid option. How could you fail at something so simple? Just go home... I can't bear to look at you anymore......")
    exit()

# Ask the user for their input [Y/N]

user_input = str(input("Welcome to the dice game! Would you like to roll a dice? [Y/N]: ").lower())

if user_input == "y":

# while True loop for the program to run a 6 sided dice roll until the user says "no"

    while True:
        print("\nRolling the dice...")
        time.sleep(3)
        print(f"The dice landed on {random.randint(1,6)}.")
        user_input = str(input("\nRoll again? [Y/N]: ")).lower()
        if user_input == "y":
            continue
        elif user_input == "n":
            user_input = str(input("Oh. Are you sure......? [Y/N]: ").lower())
            if user_input == "y":
                break
            elif user_input == "n":
                print("\nThen let's keep playing!!")
                continue
            else:
                invalid_option()
        else:
            invalid_option()
elif user_input == "n":
    print("\nThen get out of here already.")
    exit()
else:
    invalid_option()

print("\nOh... I see...... Thanks for playing :( Goodbye.")