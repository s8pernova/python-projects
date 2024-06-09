import random
import time

points_to_win = 2
opponent = "THE CONSOLE"
user_score = 0
opponent_score = 0

def wait_2():
    time.sleep(2)

def wait_4():
    time.sleep(4)

def invalid_option():
    print("\nThat's not a valid option. The referee notices this and instantly disqualifies you.")
    wait_4()
    print("Luckily, you had enough money to bribe him, and he let you try again.")
    wait_2()

def win():
    print(f"\n...but it's not very effective against your {user_input}! You won this round.")
    wait_2()
    global user_score # I had to learn how to use global variables in order to make this work but it was worth it
    user_score += 1

def lose():
    print(f"\nAnd it's super effective against your {user_input}!! You lost this round :(")
    wait_2()
    global opponent_score
    opponent_score += 1

def tie():
    wait_2()

outcomes = [[tie, lose, win], [win, tie, lose], [lose, win, tie]]

print("Welcome to the ultimate Rock-Paper-Scissors tournament V2!")
wait_4()
print(f"\nWhoever gets to {points_to_win} points first wins the tournament.")
wait_4()
print(f"\nYour opponent for this match is... {opponent}!!")

while True:
    wait_4()
    print("\nThe next round will start in 3...", end = " ")
    time.sleep(1.25)
    print("2...", end = " ")
    time.sleep(1.25)
    print("1...")
    time.sleep(1.25)
    print("\nGO!!")
    time.sleep(1.25)

    options = ["rock", "paper", "scissors"]

    while True: # Originally I was going to use "try" and "except" but I couldn't find out how to make it work with the options list so I just used another while true loop
        user_input = str(input("\nChoose your fighter! [Rock/Paper/Scissors]: ").lower())

        if user_input in options:
            break
        else:
            invalid_option()
    
    opponent_input = str(random.choice(options)) # I was thinking about doing [comp_choice -1] like in the video, but I found that this also works really well for my program

    outcome = outcomes[options.index(user_input)][options.index(opponent_input)] # I did .index to make the user input work by typing in a str instead of 1, 2, or 3 for rock paper or scissors

    if outcome != tie:
        print(f"\nYour opponent chose {opponent_input}!")
    else:
        print(f"\nYour opponent also chose {opponent_input}! How anti-climactic.")
    
    wait_2()
    
    outcome()

    if user_score > opponent_score:
        lead_player = "You're"
    elif user_score < opponent_score:
        lead_player = "Your opponent"

    print(f"\nThe score is currently {user_score} to {opponent_score}.")
    if user_score < points_to_win and opponent_score < points_to_win and user_score != opponent_score:    
        print(f"{lead_player} in the lead!")

    wait_2()

    if user_score >= points_to_win:
        print("\nAnd it looks like you won the tournament!! Good job.")
        break
    elif opponent_score >= points_to_win:
        print("\n...And you also lost the tournament. That's embarrassing.")
        break
    
wait_4()

print("\nThanks for playing! Goodbye.")