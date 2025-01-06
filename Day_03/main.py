# Learning Control Flow and Logical Operators

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right'\n").lower()

if direction == 'left':
    print("You approached a lake. There is an island in the middle of the lake")
    choice = input("Type 'swim' to swim across or 'wait' to wait for a boat\n").lower()

    if choice != "wait":
        print("You were attacked by a trout. Game over!")
    else:
        print("You arrived at the island unharmed."
              "There is a house with 3 doors.One red, one yellow, one blue.")
        door = input ("Which colour do you choose? Type: 'red', 'yellow' or 'blue'\n").lower()
        if door == 'Red':
            print("You were burned by fire. Game over!")
        elif door == 'Yellow':
            print("You found the treasure. You win!")
        elif door == 'Blue':
            print("You were eaten by beasts. Game over!")
        else:
            print("Game over!")

else:
    print("You fell into a hole. Game over!")