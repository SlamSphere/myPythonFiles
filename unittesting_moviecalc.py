'''
calculateInitialBill(num_of_people)
- Start with the regular price of $10 per person
- Multiply the number of people by 10 to get the initial bill
'''

'''
applyMemberDiscount(price, members)
- Ask if there are any members
- If there are members
    Apply a 5% discount to the price
- Otherwise, leave the price unchanged
'''

'''
applyVolumeDiscount(price, num_of_people)
- If the number of people is 8 or more
    Apply a 10% group discount to the price
- Otherwise, leave the price unchanged
'''

'''
addSalesTax(price)
- Apply 8% sales tax to the price
- Return the final price after tax
'''
import sys
import unittest

movieName = input("Name of Movie? ")
num_of_people = int(input("How many people are watching today? "))
members = input("Are there any members present? (enter yes or no, lowercase only): ")

if num_of_people < 0:
    print("Your number is invalid!!")
    sys.exit(1)
if num_of_people == 0:
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

price = calculateInitialBill(num_of_people)
price = applyMemberDiscount(price, members)
price = applyVolumeDiscount(price, num_of_people)
price = addSalesTax(price)

print("Your price is $", f"{price:.2f}")

def check_input_is_number():
    assert isinstance(num_of_people, int)

suite = unittest.TestSuite()
suite.addTest(unittest.FunctionTestCase(check_input_is_number))

def run_tests():
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()

'''
num-of-people, Members?
0, n/a, Eo: $0, Po: $0
-1, n/a, Eo: system print invalid, Po: system print invalid
1, yes, Eo: $10.26, Po: $10.26
2, nope, Eo: $21.60, Po: $21.60
8, yes, Eo: $73.87, Po: $73.87
8, no, Eo: $77.76, Po: $77.76
'''