#SharonnaEvick
#07/14/2025
#P5LAB
# This program simulates a self-checkout machine.
# It generates a random total amount owed and prompts the user to enter payment.
# If the user provides enough money, the program calculates and displays the change.
# The change is broken down into dollars, quarters, dimes, nickels, and pennies


import random

def disperse_change(change):
    # Convert to cents
    change_in_cents = round(change * 100)

    # Coin values in cents
    dollars = change_in_cents // 100
    change_in_cents %= 100

    quarters = change_in_cents // 25
    change_in_cents %= 25

    dimes = change_in_cents // 10
    change_in_cents %= 10

    nickels = change_in_cents // 5
    change_in_cents %= 5

    pennies = change_in_cents

    # Display the result
    print("\nChange to return:")
    print(f"Dollars : {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes   : {dimes}")
    print(f"Nickels : {nickels}")
    print(f"Pennies : {pennies}")

def main():
    # Generate random float for total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"\nYou owe: ${total_owed:.2f}")

    # Prompt user for how much they will enter
    cash_given = float(input("How much cash will you put into the self checkout: $"))

    # check if user has gives enough
    while cash_given < total_owed:
        print("Insufficient amount. Please enter enough cash.")
        cash_given = float(input("Enter the amount of cash given: $"))

    # Calculate change
    change = round(cash_given - total_owed, 2)
    print(f"Change is: ${change:.2f}")

    # Disperse change
    disperse_change(change)

# Call main function
main()
