'''
Ask for the movie name
Ask how many people are watching
If the number of people is less than 0, it’s invalid  
    Print an error message  
    Stop the program  
If the number of people is 0  
    Print that the price is $0  
    Stop the program  
Otherwise, start with the regular price of $10 per person
Ask if there are any members
If there are members  
    Apply a 5% discount  
If the number of people is 8 or more  
    Apply a 10% group discount  
Apple 8 % sales tax
Print the final price after all discounts
'''
import sys   
movieName = input("Name of Movie? ")
num_of_people = int(input("How many people are watching today? "))
members = input("Are there any members present? (enter yes or no, lowercase only): ")
if num_of_people < 0:
    print("Your number is invalid!!")
    sys.exit(1)
if (num_of_people == 0):
    print("Your price is $0")
    sys.exit(0)
def calculateInitialBill(num_of_people):
    return num_of_people * 10
def applyMemberDiscount(price, members):
    if members == "yes":
        return price * 0.95
    return price
def applyVolumeDiscount(price, num_of_people):
    if num_of_people >= 8:
        return price * 0.90
    return price
def addSalesTax(price):
    return price * 1.08
members = input("Are there any members present? (enter yes or no, lowercase only): ")
price = calculateInitialBill(num_of_people)
price = applyMemberDiscount(price, members)
price = applyVolumeDiscount(price, num_of_people)
price = addSalesTax(price)
print("Your price is $", f"{price}")
'''
num-of-people, Members?
0, n/a, Eo: $0, Po: $0
-1, n/a, Eo: system print invalid, Po: system print invalid
1, yes, Eo: $10.26, Po: $10.26
2, nope, Eo: $21.60, Po: $21.60
8, yes, Eo: $73.87, Po: $73.87
8, no, Eo: $77.76, Po: $77.76
'''
