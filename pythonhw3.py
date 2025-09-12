#the program starts off with asking the user for their desired inputs.
# the program the check if a is between b and c whether or not b or c is the greater one
# if the first number is not between the two, then it will say that the number is not in range of the two numbers.
import math
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))
if (a >= b and a <= c) or (a >= c and a >= b):
    print("The first number is in the range of the other two.")
else:
    print("The first number is NOT in the range of the other two.")
#Test Cases
#5, 2, 10
#12, 3, 9
#7, 7, 10
#3, 3, 3
# because all of these test cases work the program will work
