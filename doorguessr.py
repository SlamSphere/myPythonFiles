#If the player enters how many doors they want, the program makes that many doors and picks one random winning door.
#If the number of doors is less than 1 or greater than 50 say that it is an invalid choice.
#If the player chooses a door within the valid range, the program opens that door and shows all doors again.
# If the chosen door is the winning door, the program says “You found the right door!” and the game ends.
# Else the program says “Wrong door, try again!” and continues.
#Else (if the guess is invalid), the program says “Invalid choice, try again.”
import random
num_doors = int(input("How many doors do you want in the game? "))
if (num_doors > 50):
    print("Invalid choice")
elif (num_doors < 1):
    print("Invalid Choice")
winning_door = random.randint(1, num_doors)
doors = ["-"] * num_doors
for i in range(num_doors):
    print(f"{i+1}) {doors[i]}")
found = False
while not found:
    guess = int(input("Choose a door number to open: "))
    if 1 <= guess <= num_doors:
        doors[guess - 1] = "*"
        for i in range(num_doors):
            print(f"{i+1}) {doors[i]}")
        print()
        if guess == winning_door:
            print("You found the right door!")
            found = True
        else:
            print("Wrong door")
    else:
        print("Invalid choice")

#Test Cases
#numofdoors,doorguesses,Eo,Po
#1,1, You found the right door!, You found the right door!
#5,2 3 1, Wrong Door Wrong Door You found the right door!, Wrong Door Wrong Door You found the right door!
#10, 10, You found the right door!, You found the right door!
#0, n/a, Invalid choice, Invalid choice
#-1, n/a, Invalid choice, Invalid choice
#5, 1, You found the right door!, You found the right door!


