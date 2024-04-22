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

print('Welcome to the classic game of "Rock, Paper, Scissors".')
game_images = [rock, paper, scissors]
user_choice = int(input('What is your choice? Type "0" for rock, "1" for paper, and "2" for scissors. \n'))
if user_choice >= 3 or user_choice < 0:
    print("You've entered an invalid choice.")
elif user_choice == 0:
    print("You chose rock.")
elif user_choice == 1:
    print("You chose paper.")
elif user_choice == 2:
    print("You chose scissors.")
print(game_images[user_choice])

cpu_choice = random.randint(0, 2)
if cpu_choice == 0:
    print("Computer chose rock.")
elif cpu_choice == 1:
    print("Computer chose paper.")
elif cpu_choice == 2:
    print("Computer chose scissors.")
print(game_images[cpu_choice])

if user_choice == 0 and cpu_choice == 2:
    print("Well done, you win!")
elif cpu_choice == 0 and user_choice == 2:
    print("Oh no, you lose.")
elif user_choice > cpu_choice:
    print("Well done, you win!")
elif user_choice < cpu_choice:
    print("Oh no, you lose.")
elif user_choice == cpu_choice:
    print("It's a draw!")
