# Program to calculate average and greatest monthly expenses

import sys

num_of_months = int(input("How many months do you want to track? "))

if (num_of_months <= 0):
    print("Your number is impossible")
    sys.exit(1)

sum = 0
greatest_expense = 0

for i in range(num_of_months):
    expense = int(input("What was your expense? "))

    if expense < 0:
        print("Invalid expense")
        sys.exit(2)

    sum = sum + expense

    if expense > greatest_expense:
        greatest_expense = expense

average = sum / num_of_months

print("The greatest expense is:", greatest_expense)
print("The total average expense is:", average)

# In English:
# - Ask user for number of months
# - If number of months is less than 0 → invalid
# - Set sum = 0 and max = 0
# - For each number of months:
#     - Ask for expense
#     - If expense is less than 0 → invalid
#     - Add expense to sum
#     - If expense is greater than max → set max = expense
# - Print the greatest expense
# - Print the total average (sum / number of months)

# ----------------------------
# Test Cases (x = months, y = expenses)
#
# num_of_months | expenses         | Expected Output (E)          | Program Output (P)
# -----------------------------------------------------------------------------
# 2             | 1, 5             | E: avg=3.0, max=5            | P: avg=3.0, max=5
# 1             | 5                | E: avg=5, max=5              | P: avg=5, max=5
# 0             | n/a              | E: Error                     | P: Error
# 1             | -2               | E: Error                     | P: Error
# 2             | 2, 6             | E: avg=4.0, max=6            | P: avg=4.0, max=6

