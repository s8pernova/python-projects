import random
import time

def invalid_option():
    print("\nThat's not a valid option. How could you fail at something so simple? Just go home... I can't bear to look at you anymore......")
    exit()

counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0

roll_counter = 600

user_input = str(input(f"Welcome to the dice game! Would you like to roll a dice {roll_counter} times? [Y/N]: ").lower())

if user_input == "y":
    print("\nRolling the dice...")
    time.sleep(3)
    for _ in range(roll_counter):
        roll = random.randint(1,6)
        if roll == 1:
            counter_1 += 1
        elif roll == 2:
            counter_2 += 1
        elif roll == 3:
            counter_3 += 1
        elif roll == 4:
            counter_4 += 1
        elif roll == 5:
            counter_5 += 1
        elif roll == 6:
            counter_6 += 1
elif user_input == "n":
    print("\nThen get out of here already.")
    exit()
else:
    invalid_option()

print(f"\nNumber of times 1 was rolled: {counter_1} \nPercentage is {(counter_1/600)*100}%")
print(f"\nNumber of times 2 was rolled: {counter_2} \nPercentage is {(counter_2/600)*100}%")
print(f"\nNumber of times 3 was rolled: {counter_3} \nPercentage is {(counter_3/600)*100}%")
print(f"\nNumber of times 4 was rolled: {counter_4} \nPercentage is {(counter_4/600)*100}%")
print(f"\nNumber of times 5 was rolled: {counter_5} \nPercentage is {(counter_5/600)*100}%")
print(f"\nNumber of times 6 was rolled: {counter_6} \nPercentage is {(counter_6/600)*100}%")

print("\nThanks for playing! Goodbye.")