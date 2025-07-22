# Shae E.
# July 14, 2025
# P3HW2 – Salary Calculator with Sentinel & Totals
# This program calculates and displays each employee’s pay including overtime.
# It repeats until the user enters "Done", and displays a summary at the end.

# 1. Get employee's name
# 2. Get number of hours worked
# 3. Get pay rate
# 4. If hours > 40:
#     a. Calculate overtime hours and overtime pay
#     b. Regular pay is for 40 hours
#    Else:
#     a. No overtime
#     b. Regular pay is all hours * pay rate
# 5. Add regular pay and overtime pay to get gross pay
# 6. Display all pay details
# ---------------------------------------------

# Prompt user for input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Define regular hours and overtime rate
REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

# Calculate regular and overtime hours
if hours_worked > REGULAR_HOURS:
    overtime_hours = hours_worked - REGULAR_HOURS
    regular_hours = REGULAR_HOURS
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate pays
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * OVERTIME_MULTIPLIER
gross_pay = regular_pay + overtime_pay

# Output result
print("\n------------------------------")
print(f"Employee name:  {employee_name}")
print()
print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay   Gross Pay")
print("--------------------------------------------------------------------------")
print(f"{hours_worked:<13}{pay_rate:<9}{overtime_hours:<10}{overtime_pay:<14.2f}${regular_pay:<13.2f}${gross_pay:.2f}")
