# 100 days of Python Project
# Project 5 -- Password Generator


import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '&', '*', '+', '(', ')']
list1=[]

print("#### WELCOME TO PASSWORD GENERATOR ####")
letter_no = int(input("\n How many letters you want in your password?\n ->"))
digit_no = int(input("How many numbers you want in your password?\n ->"))
symbol_no = int(input("How many symbols you want in your password?\n ->"))

for i in range(0,letter_no):
  list1.append(random.choice(letter))

for i in range(0,digit_no):
  list1.append(random.choice(digit))

for i in range(0,symbol_no):
  list1.append(random.choice(symbol))
# print(list1)
# random shuffle module will change the sequence of the list
random.shuffle(list1)
print("\nHere is your password :")
for i in list1:
  print(i,end="")

print("\n\nThanks for using Password Generator !!!")