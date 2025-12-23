import random

x = 0
coinrow = []

while (x < 20):
    index = random.randint(0, 1)
    coinrow.append(index)
    x = x + 1

P1 = random.randint(0, 19)
P2 = random.randint(0, 19)

while (P1 == P2):
    P1 = random.randint(0, 19)
    P2 = random.randint(0, 19)

print("Player 1 you are at", P1, "Player 2 you are at", P2)

num_of_turns = 0
P1total = coinrow[P1]
P2total = coinrow[P2]

while (num_of_turns < 6):
    P1input = int(input("Enter your number of turns(-1 turn left, 1 to move right): "))

    while (coinrow[P1] == 0) and (P1input == -1):
        P1input = int(input("Sorry your number is invalid and you must reenter a different move"))

    while (coinrow[P1] == 19) and (P1input == 1):
        P1input = int(input("Sorry your number is invalid and you must reenter a different move"))

    while (P1input != 1) and (P1input != -1):
        P1input = int(input("Sorry your turn is not possible!"))

    if (P1input == -1):
        P1 = P1 - 1
    if (P1input == 1):
        P1 = P1 + 1

    P1total = P1total + coinrow[P1]
    print("Player 1 your score is", P1total)

    P2input = int(input("Enter your number of turns(-1 to move left and 1 to move right): "))

    while (coinrow[P2] == 0) and (P2input == -1):
        P2input = int(input("Sorry you entered an invalid number you must reenter a turn"))

    while (coinrow[P2] == 19) and (P2input == 1):
        P2input = int(input("Sorry you entered an invalid number you must reenter a turn"))

    while (P2input != 1) and (P2input != -1):
        P2input = int(input("Sorry your turn is not possible!"))

    if (P2input == -1):
        P2 = P2 - 1
    if (P2input == 1):
        P2 = P2 + 1

    P2total = P2total + coinrow[P2]
    print("Player 2 your score is", P2total)

    num_of_turns = num_of_turns + 1

if (P1total > P2total):
    print("Player 1 you have won")
elif (P2total > P1total):
    print("Player 2 you have won")
else:
    print("There is no winner")