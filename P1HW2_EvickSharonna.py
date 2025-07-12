# Evick Sharonna
# Date: 10/13/2024
# Assignment Name: P1HW2_EvickSharonna
# This program calculates the total expenses for a trip and displays
# the remaining budget after subtracting the expenses from the user's budget.

# Pseudocode:
# 1. Prompt the user to enter their total budget.
# 2. Prompt the user to enter their travel destination.
# 3. Prompt the user to enter the amount they will spend on gas.
# 4. Prompt the user to enter the amount they will spend on accommodation.
# 5. Prompt the user to enter the amount they will spend on food.
# 6. Add up all expenses (gas, accommodation, food) to get total expenses.
# 7. Subtract the total expenses from the budget to calculate the remaining budget.
# 8. Display the trip destination, total budget, total expenses, and remaining budget.

# Ask user to enter their budget
budget = float(input("Enter your budget for the trip: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for the amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Ask user for the amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Ask user for the amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display results
print("\nTrip Budget Analysis")
print(f"Destination: {destination}")
print(f"Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
