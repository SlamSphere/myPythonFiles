import random
import sys
import math

# Game: Guess a number using random.randint(0, 100000)

# In English:
# 1. Generate a random number from 1–100000
# 2. Ask the user for their guess (each input is between 1–100000)
# 3. Until the guess equals the random number:
#       - Say if the number is greater or less than the generated number
# 4. If the number is equal to the generated number:
#       - Print "You got it!" and stop

x = random.randint(0, 100000)

while True:
    guess = int(input("What is your guess? "))
    if guess < x:
        print("Your number is smaller")
    elif guess > x:
        print("Your number is bigger")
    else:
        print("You got it!")
        sys.exit(0)

# -------------------------------------------------
# Test Cases
#
# x = 2, guess = 1
# Expected: "Your number is smaller than the number I got."
# Program:  "Smaller than the number I got."
#
# x = 2, guess = 3
# Expected: "Your number is bigger than the number I got."
# Program:  "Your num is bigger than mine."
#
# x = 2, guess = 2
# Expected: "You got it!"
# Program:  "You got it!"
# -------------------------------------------------

# Repeat (loop explanation):
# Ask for the number
#   if the number chosen < program’s number → print "Your number is bigger"
#   else if the number chosen > program’s number → print "Your number is smaller"
#   else → print "You got it!" and stop
