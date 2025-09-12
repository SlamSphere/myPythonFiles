# Find Average of Monthly Expenses
#In English
# Ask user how many months are being tracked
# Ask the user the monthly expense for each month
# Add all the monthly expenses
# Divide all by the number of months

import sys
import math

sum = 0
input_months = int(input("How many months? "))

# Input Validation
if input_months <= 0:
    print("Invalid entry")
    sys.exit(1)

for i in range(input_months):
    expense = int(input("What was your expense? "))

    if expense < 0:
        print("Invalid expense")
        sys.exit(2)

    sum = sum + expense

Average = sum / input_months
print(Average)

# ----------------------------
# Test Cases (x = months, y = monthly expenses)
#
# input_months | expenses       | Expected Output (E) | Program Output (P)
# ------------------------------------------------------------------------
# 2            | 1, 2           | E: 1.5              | P: 1.5
# 0            | n/a            | E: Error            | P: Error
# 1            | 2              | E: 2                | P: 2
# 1            | -2             | E: Error            | P: Error
# -1           | n/a            | E: Error            | P: Error
# 2            | 2, 2           | E: 2                | P: 2

