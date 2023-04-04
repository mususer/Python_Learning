#This code is randomly generating heads or tails for the user.
#importing random module
import random
result = random.randint(0,1)
if result == 0:
    print("Tails")
else:
    print("Heads")