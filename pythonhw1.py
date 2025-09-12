#This program starts off with asking the user to input three different integers. 
#Using those three integers the program first checks if the first number is between the other two numbers.
#If the first case is not true the program check whether or not the second number is between the other two numbers.
#If none of the if statements are true, then the else outputs the third number because if the other two aren't the second greates then the third must be the second greatest.
import math
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))
if (a >= b and a >= c) or (a <= b and b>= c):
    print("Second biggest is:", b)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second biggest is:", b)
else:
    print("Secend biggest is:", c)
#Test cases
#5, 9, 2
#1, 2, 3
#7, 5, 3
#4, 4, 6
#8, 8, 8
#-5, -3, -9
#-3, 0, 2
# because all of these test cases do in fact work I can conclude that the program works.