# PART 1

# integer
bottles_of_water_today = 1
print(bottles_of_water_today)

# string
how_I_am_feeling_right_now = "pretty good"
print(how_I_am_feeling_right_now)

# float
how_much_money_I_have_currently = 20.53
print(how_much_money_I_have_currently)

# boolean
will_I_graduate_this_course = True
print(will_I_graduate_this_course)

# PART 2

first_name = input("\nWhat is your first name?: ")
bottles_water = int(input(f"Hi, {first_name}. How many bottles of water did you have today?: "))
feelings_now = str(input(f"{bottles_water} doesn't sound like a lot, I think you should drink more. How are you feeling right now?: "))
money = float(input(f"Feeling {feelings_now}? Maybe having more money would make you happier. How much do you have right now?: "))
graduating_this_year = bool(input("Do you think you'll pass this course? (True/False): "))
print("\nJust kidding I don't really care. I'm just a robot")

# PART 3

print("\nThe type for the bottles of water you had is called", type(bottles_of_water_today))
print(f"The type for how you're feeling is called {type(how_I_am_feeling_right_now)}")
print(f"The type for how much money you have is called {type(how_much_money_I_have_currently)}")
print("The type for whether you'll graduate is called", type(will_I_graduate_this_course))