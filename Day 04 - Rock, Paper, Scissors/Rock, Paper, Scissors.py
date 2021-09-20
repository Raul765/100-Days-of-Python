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

import random

options=[rock,paper,scissors]

player=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")

computer=random.randint(0,2)

if player in ["0","1","2"]:

  player=int(player)

  print(f"You chose \n {options[player]}")
  print(f"Computer chose \n {options[computer]}")

  if player==computer:
    print("Draw")
  elif abs(player-computer)==1:
    if player > computer:
      print("You won")
    else:
      print("You lost")
  else:
    if player > computer:
      print("You lost")
    else:
      print("You won")

else:
  print("Invalid entry, you lost!")