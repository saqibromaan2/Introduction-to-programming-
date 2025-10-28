# Dictionary mapping month numbers to the number of days
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user to enter a month number
month = int(input("Enter a month number (1-12): "))

# Check if the month number is valid
if month in month_days:
    print(f"Month {month} has {month_days[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
