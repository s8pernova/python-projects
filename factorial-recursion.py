# Program to find the factorial of a number and print it out

# Ask the user for what the number that they want to factorial is
def ask_for_int():
    while True:
        # try/except statement for if the user decides to be funny and enter a string or something
        try:
            num = int(input("What number would you like to factorial?: "))
            if num < 0:
                raise ValueError
            elif num > 995:
                # I did some testing and found out that the biggest number I could do was 998 recursions before the system gave me an error. So I just made it so that the user can't do more than 995
                print("That's way too big of a number..,....,,...,,... Pick a smaller one.\n")
            else:
                return num
        except ValueError as err:
            print(f"Enter a positive integer d00d. {err}\n")

# Factorial the chosen number using the recursive method. This is really self-explanatory but I still want to add in comments
def factorial(num):
    if num == 0 or num == 1:  # Base case
        return 1
    else:
        return num * factorial(num - 1)

# Print out the factorial result    
def print_factorial(original_num, result):
    print(f"The factorial of {original_num} is {result}.")

def main():
    original_num = ask_for_int()
    result = factorial(original_num)
    print_factorial(original_num, result)


if __name__ == "__main__":
    main()