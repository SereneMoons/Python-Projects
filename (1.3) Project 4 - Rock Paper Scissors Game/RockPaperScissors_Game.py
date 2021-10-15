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
tools = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors!")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
cpu_choice = random.randint(0,2)

if player_choice < 0 or player_choice > 3:
  print("You typed an invalid Value.")
else:  
  print(tools[player_choice])
  print("Computer Chose: ")
  print(tools[cpu_choice])

if player_choice == 0:
  if cpu_choice == 0:
    print("You Tied!")
  elif cpu_choice == 1:
    print("You Lose :(")
  elif cpu_choice == 2:
    print("You Win!!!")
elif player_choice == 1:
  if cpu_choice == 0:
    print("You Win!!")
  elif cpu_choice == 1:
    print("You Tied!")
  elif cpu_choice == 2:
    print("You Lose :(")
elif player_choice == 2:
  if cpu_choice == 0:
    print("You Lose :(")
  elif cpu_choice == 1:
    print("You Win!!!")
  elif cpu_choice == 2:
    print("You Tied!")

