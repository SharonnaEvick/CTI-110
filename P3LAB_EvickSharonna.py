# --------------------------------------------------
#P3LAB_EvickSharonna
# This program calculates the fewest number of coins needed to make a given amount of money.
# --------------------------------------------------

# Get money input and convert to cents
amount = float(input("Enter amount of money as a float (e.g., $1.45): ").replace("$", ""))
cents = int(round(amount * 100))  # convert to integer cents

if cents == 0:
    print("No change")
else:
    # Dictionary to store coin values in cents
    coin_values = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }
# Check for zero
if cents == 0:
    print("No change")
else:
    # Calculate and print coins
    for coin, value in coin_values.items():
        count = cents // value
        if count > 0:
            cents -= count * value
            name = coin if count == 1 else ("pennies" if coin == "penny" else coin + "s")
            print(f"{count} {name}")
   
