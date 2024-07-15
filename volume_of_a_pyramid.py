import time

# Ask the user for the length, width, and height of the pyramid

length = input("Enter the length of the pyramid's base: ")
width = input("Enter the width of the pyramid's base: ")
height = input("Enter the height of the pyramid: ")

print("\nPlease wait a sec so I can calculate this for you...")

time.sleep(3)

# Calculate the volume

volume = (float(length) * float(width) * float(height)) / 3
volume_rounded = round(volume, 2)

# Display the result

print(f"\nFinished. The volume of the pyramid is {float(volume_rounded)}")
print("*Note that this answer was rounded to the nearest 2 decimal places")