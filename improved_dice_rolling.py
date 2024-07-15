import time
import random

# Defining built-in variables the user cannot change

min_rolls = 1
max_rolls = 1000000

min_sides = 1
max_sides = 20

pick_sides_number = f"Enter a number between {min_sides} and {max_sides}."

# while True loop to make the program last forever until user input to stop

while True:

# while True loop to house the try/except for how many dice the user wants to roll

    while True:
        try:
            amount_of_rolls = int(input("How many die would you like me to roll?: "))
            
            if amount_of_rolls >= min_rolls and amount_of_rolls <= max_rolls:
                break
            elif amount_of_rolls > max_rolls:
                print("Nope. Nopenopenope. Anything above a million rolls is way too much. Try again.")
                print()
            elif amount_of_rolls < min_rolls:
                print("That's too few rolls... Try entering a positive number.")
                print()
        except:
            print(f"Invalid input d00d. Just pick a number greater than {min_rolls}.")
            print()

# while True loop to house the try/except for how many sides the user wants the dice to have

    while True:
        try:
            number_of_sides = int(input(f"How many sides should the dice have? [{min_sides}-{max_sides}]: "))
            
            if number_of_sides <= max_sides and number_of_sides >= min_sides:
                break
            elif number_of_sides > max_sides:
                print(f"That's way too many sides!! {pick_sides_number}")
                print()
            elif number_of_sides < min_sides:
                print(f"That's too few sides!! {pick_sides_number}")
                print()
        except:        
            print(f"Invalid input d00d. {pick_sides_number}")
            print()

    print("\nRolling the dice...")

    time.sleep(3)

    counters = [0] * number_of_sides # Counters for each side of the dice from the second user input

# for loop to roll the dice depending on the user input and add 1 to the counters for each roll

    for x in range(amount_of_rolls):
        roll = random.randint(0, (number_of_sides - 1))
        counters[roll] += 1

# Print the results

    for x in range(len(counters)):
        print(f"\nNumber of times {x + 1} was rolled: {counters[x]} \nThe percentage is around {round ((counters[x] / amount_of_rolls) * 100, 2)}%")
        time.sleep(0.1)

# while True loop to house if/else statements that ask if the user wants to roll again

    while True:
        user_input = str(input("\nWould you like me to roll again? [Y/N]: ").lower())

        if user_input == "n":
            print("\nMy life's mission is now complete. Goodbye.")
            exit()
        elif user_input == "y":
            print()
            break
        else:
            print("Invalid input d00d. Enter Y or N.")