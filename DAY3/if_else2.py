#This code will test the compatibility between two people

#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

new_name1 = name1.lower()
new_name2 = name2.lower()

# count function will count how many times the given letter is present the string
value1 = str(new_name1.count('t') + new_name1.count('r') + new_name1.count('u') + new_name1.count('e') + new_name2.count('t') + new_name2.count('r') + new_name2.count('u') + new_name2.count('e'))
value2 = str(new_name1.count('l') + new_name1.count('o') + new_name1.count('v') + new_name1.count('e') + new_name2.count('l') + new_name2.count('o') + new_name2.count('v') + new_name2.count('e'))

value = int(value1 + value2)

if value < 10 or value > 90:
    print(f"Your score is {value}, you go together like coke and mentos.")
elif value > 40 and value < 50:
    print(f"Your score is {value}, you are alright together.")
else:
    print(f"Your score is {value}.")

