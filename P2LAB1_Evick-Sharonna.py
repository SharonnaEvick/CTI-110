import math
# Evick Sharonna
# Date: 10/27/2024
# Assignment Name: P2LAB1_EvickSharonna
# This program will calculate the diameter, circumference, and area of a circle


# Get radius input from the user as a float
radius = float(input("What is the radius of the circle?: "))

# Calculate diameter, circumference, and area using the provided formulas
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with the specified formatting
print(f"The diameter of the circle is: {diameter:.1f}")           # Diameter with 1 decimal place
print(f"The circumference of the circle is: {circumference:.2f}")  # Circumference with 2 decimal places
print(f"The area of the circle is: {area:.3f}")                    # Area with 3 decimal places
