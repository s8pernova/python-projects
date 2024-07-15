import time

# Defining functions

def wait():
    time.sleep(3)

def invalid_option():
    print("\nThat's... uh.... not a valid option.......... that's embarrasing.......................")
    exit()

def goodbye():
    print("\nFINE! It's not like saying 'hello' was my only function or anything...... GOODBYE!")

# Ask the user for their input [Y/N]

user_input = str(input("Hello, and welcome to the 'Hello Machine 3000'! Would you like me to say 'hello'? [Y/N]: ").lower())

if user_input == "y":

# while True loop for the program to infinitely print "hello" until the user says "no"

    while True:
        print("\nHello!")
        wait()
        user_input = str(input("Would you like me to say it again...? [Y/N]: ").lower())
        if user_input == "y":
            continue
        elif user_input == "n":
            user_input = str(input("\nWait, are you serious......? [Y/N]: ").lower())
            if user_input == "y":
                goodbye()
                break
            elif user_input == "n":
                print("Then let's keep the streak going!!")
                continue
            else:
                invalid_option()
        else:
            invalid_option()
elif user_input == "n":
    goodbye()
else:
    invalid_option()