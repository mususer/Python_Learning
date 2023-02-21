# This code is checking the highest number in the list
number = input("Input a list of numbers ").split()
for n in range(0, len(number)):
  number[n] = int(number[n])
  
print(number)
max = 0

for i in number:
    if i > max:
        max = i
print(f"The highest number is : {max}")