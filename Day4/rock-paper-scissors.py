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

game_images = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(game_images[users_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

if users_choice >= 3 or users_choice <0:
    print("You typed an invalid number, you lose!")
elif users_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and users_choice == 2:
    print("You Lose!")
elif computer_choice > users_choice:
    print("You Lose!")
elif users_choice > computer_choice:
    print("You Win!")
elif computer_choice == users_choice:
    print("Its a draw!")