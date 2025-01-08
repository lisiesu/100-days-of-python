import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice < 0 or user_choice > 2:
    print("You entered an invalid number. You lose")
    exit()
else:
    print(options[user_choice])

computer_choice = random.choice(options)
print(f"Computer chose:\n{computer_choice}")

if user_choice == 0:
    if computer_choice == rock:
        print("It's a draw!")
    elif computer_choice == paper:
        print("You lose!")
    else:
        print("You win!")

elif user_choice == 1:
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("It's a draw!")
    else:
        print("You lose!")

elif user_choice == 2:
    if computer_choice == rock:
        print("You lose!")
    elif computer_choice == paper:
        print("You win!")
    else:
        print("It's a draw!")

else:
    print("You typed an invalid number. You lose!")