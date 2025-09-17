#If the player enters how many doors they want, the program makes that many doors and picks one random winning door.
#If the player chooses a door within the valid range, the program opens that door and shows all doors again.
# If the chosen door is the winning door, the program says “You found the right door!” and the game ends.
# Else the program says “Wrong door, try again!” and continues.
#Else (if the guess is invalid), the program says “Invalid choice, try again.”
import random
num_doors = int(input("How many doors do you want in the game? "))
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
#1,1, 
#5,2 3 1, 
#10, 10, 
#0, n/a,
#-1, n/a,
#5. 1,


