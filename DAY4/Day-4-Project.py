# 100 days of Python Project
# Project 4 -- Rock,paper and scissors

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

# print(type(rock))
user = int(input(" What did you choose?? \n Type 0 for Rock\n Type 1 for Paper \n Type 2 for Scissors\n -> "))
print(" ")

#using if condition to print rock,paper,scissors image 
if user == 0:
  print(f"ROCK\n{rock}")
elif user == 1:
  print(f"PAPER\n{paper}")
else:
  print(f"SCISSORS\n{scissors}")
  
#using random module to generate number for computer
comp = random.randint(0,2)
if comp == 0:
  print(f"ROCK\n{rock}")
elif comp == 1:
  print(f"PAPER\n{paper}")
else:
  print(f"SCISSORS\n{scissors}")

if user == comp:
  print("It's a Draw !!!")
elif user == 0:
  if comp == 1:
    print("You Lose, computer wins !!")
  else:
    print("You win !!!")
elif user == 1:
  if comp == 0:
    print("You win !!!")
  else:
    print("You Lose, computer wins !!")
else:
  if comp == 0:
    print("You Lose, computer wins !!")
  else:
    print("You win !!!")
    