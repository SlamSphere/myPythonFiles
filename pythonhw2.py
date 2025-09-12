#The program first starts off with asking the user to input the sides of the triangle
#the program then checks if all the sides are equal to each other. if so the triangle is equilatera
#Then the program checks if the triangle has onl two equal sides, if so the triangle is isosceles
#if all the sides are not equal the triangle becomes scalene.
import math
a = int(input("Enter your first side:"))
b = int(input("Enter your second side:"))
c = int(input("Enter your third side:"))
if a == b and b== c:
    print("The triangle is Equailateral")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
#Test Cases
#5, 5, 5
#7, 7, 6
#6, 8, 10
#4, 6, 6
#3, 4, 5
# all of these inputs do run the expected output
#this program could be enhanced by checking if the triangle can actually be a triangle with triangle inequality theorem.
