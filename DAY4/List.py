# This code is using list and random module to display random name from a list that user entered
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
size = len(names)
i = random.randint(0,size-1)
name = names[i]
print(f"{name} is going to buy the meal today!")


