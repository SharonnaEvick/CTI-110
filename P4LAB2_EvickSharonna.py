# P4LAB2_EvickSharonna.py

# Start while loop to allow repeating the program
run_again = "yes"

while run_again.lower() == "yes":
    user_input = input("Enter an integer: ")

    # Check if the input is an integer
    if user_input.lstrip("-").isdigit():
        number = int(user_input)

        if number >= 0:
            print(f"\nMultiplication table for {number}:")
            for i in range(1, 13):  # for loop for 1 to 12
                print(f"{number} x {i} = {number * i}")
        else:
            print("This program does not handle negative numbers.")
    else:
        print("That's not a valid integer.")

    # Ask if user wants to run again
    run_again = input("\nWould you like to run the program again? (yes/no): ")

print("This was fun!")
