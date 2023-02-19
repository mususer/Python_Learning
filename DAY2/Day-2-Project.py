# 100 days of Python Project
# Project 2 -- Tip calculator

print("## Welcome to the tip calculator !!! ##")

#Take bill, tip details and number of people input from user
Total_bill = input("Please enter the total amount of bill -> " )
Tip = input("How much tip would you like to give ? -> 10, 12 or 15? ")
People = input("How many people to spit the bill ? -> ")

#Type conversion -- from string to float and integer
Total_bill = float(Total_bill)
Tip = float(Tip)
People = int(People)

#Total bill calculation
Total_bill += (Total_bill*Tip)/100
Amount = round(Total_bill/People ,2)

#Printing the amount each person should pay using f-string
print(f"Each person should pay -> {Amount}")