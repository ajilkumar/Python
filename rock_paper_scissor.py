import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
pics = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
if (player >=3 or player < 0):
    print("Invalid number")
else:
    print(pics[player])
    computer = random.randint(0,2)
    print("Computer chose :")
    print(pics[computer])

    if (player == 0 and computer == 2):
        print("you win")
    elif (computer == 0 and player == 2):
        print("You loose")
    elif (computer>player):
        print("You loose")
    elif (player>computer):
        print("You win")
    elif (computer == player):
        print("It's a tie")
