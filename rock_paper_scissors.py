import time
import random

def ineffective():
    print(f"\n...But it's not very effective against your {user_input}! You win!!")
    wait()
    print("The audience cheers and you can finally go home.")
    wait()
    print("You see a shiny limousine coming out of the auditorium - draped with its majestic banners.")
    wait()
    print("A red carpet sits at the floor of the vehicle, and with it, the president of the United States.")
    wait()
    print("'I'm so proud of you!' he says, as he walks towards you with a gleaming smile.")
    wait()
    print("He's about to shake your hand, when all of a sudden...")
    wait()
    print("You wake up.")
    wait()
    print("Slowly, in your broken-down apartment, you look around as you realize...")
    wait()
    print("... Have you ever truly won?")
    wait()

def effective():
    print(f"\nAnd it's super effective against your {user_input}!! You lose :(")
    time.sleep(3)
    print("\nNext game starting...")

def tie():
    print("\nIt's a tie! Starting the next game...")

def wait():
    time.sleep(5)

def invalid_option():
    print("\nThat's not a valid option. The referee notices this and instantly disqualifies you.")
    print("You lose :(")
    exit()

print("Welcome to the ultimate Rock-Paper-Scissors tournament!")

while True:
    time.sleep(4)
    print("\nYour opponent for this round is... THE CONSOLE!!")
    time.sleep(4)
    print("\nYour match will start in")
    print("3...")
    time.sleep(1.25)
    print("2...")
    time.sleep(1.25)
    print("1...")
    time.sleep(1.25)
    print("GO!!")
    time.sleep(1.25)

    user_input = int(input("\nChoose your fighter! [Rock (1) / Paper (2) / Scissors (3)]: "))

    if user_input == 1:
        user_input = "rock"
    elif user_input == 2:
        user_input = "paper"
    elif user_input == 3:
        user_input = "scissors"
    else:
        invalid_option()

    computer_choice = int(random.randint(1, 3))

    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"

    print(f"\nYour opponent chose {computer_choice}!")
    time.sleep(2)

    if user_input == computer_choice:
        tie()
    elif user_input == "rock":
        if computer_choice == "scissors":
            ineffective()
            break
        else:
            effective()
    elif user_input == "paper":
        if computer_choice == "rock":
            ineffective()
            break
        else:
            effective()
    elif user_input == "scissors":
        if computer_choice == "paper":
            ineffective()
            break
        else:
            effective()

print("\nThanks for playing!")