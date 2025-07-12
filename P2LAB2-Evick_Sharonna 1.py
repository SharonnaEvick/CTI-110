# Evick Sharonna
# Date:06/22/2025
# Assignment Name: P2LAB2_EvickSharonna
# this program uses a dictionary to store user input and displays output to the user


# Create a dictionary with the given key-value pairs
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Print the keys of the dictionary
print("Available vehicles:", list(car_mpg.keys()))

# Prompt the user to enter a vehicle from the dictionary
vehicle = input("Enter the vehicle to see its mpg: ")

# Check if the entered vehicle exists in the dictionary
if vehicle in car_mpg:
    # Display the MPG for the chosen vehicle
    mpg = car_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")

    # Prompt the user to enter the number of miles they will drive
    miles = float(input(f"How many miles will you drive the {vehicle}? : "))

    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg

    # Display the gallons of gas needed, rounded to two decimal places
    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")
else:
    print("The entered vehicle is not available in the list. Please check the spelling and try again.")
