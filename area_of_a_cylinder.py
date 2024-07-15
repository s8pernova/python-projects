import time
import math

# Ask the user for the length, width, and height of the cylinder

radius = input("Enter the length of the cylinder's base: ")
height = input("Enter the height of the cylinder: ")

print("\nPlease wait a sec so I can calculate this for you...")

time.sleep(3)

# Calculate the area

area = (2 * math.pi * float(radius) * float(height)) + (2 * math.pi * (float(radius) ** 2))
area_rounded = round(area, 2)

# Display the result

print(f"\nFinished. The area of the cylinder is {float(area_rounded)}")
print("*Note that this answer was rounded to the nearest 2 decimal places")