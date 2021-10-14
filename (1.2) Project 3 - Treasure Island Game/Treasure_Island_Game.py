print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
first_Choice = input("You find yourself at an intersection. Do you want to go 'left' or 'right' ? \n")
first_Choice = first_Choice.lower()

if first_Choice == 'right':
  print("You suddenly encounter a Lion who devours you and you die!\nYOU LOSE!")
else:
  second_Choice = input("You find a river, do you 'swim' across or take a longer route by going 'around' ?\n")
  if second_Choice == 'swim':
    second_Choice = second_Choice.lower()
    print("Your Foot gets stuck on a Marine Plant and you drown!\nYou Lose!")
  else:
    third_Choice = input("You find three doors, a 'Green' door, a 'Yellow' door, and a 'Red' door. Which do you Choose?\n")  
    third_Choice = third_Choice.lower()
    if third_Choice == 'green':
      print("You chose the Green Door, without thinking you walk in and fall into a pit filled with Poisonous Spiders. You can't get out and die of Poisining.\nYou Lose!")
    elif third_Choice == 'yellow':
      print("You chose the Yellow Door, you walk in and get trapped inside where there's nothing but quick sand. Eventually you get engulfed and never come out.\nYou Lose!")
    else:
      print("You chose the Red Door, inside you find a treasure chest filled with nothing but gold and silver! Next to it you find a fully charged phone with service and food that will last you for a few days. Eventually you are rescued and you take the treasure home with you!\nYou Win!")
