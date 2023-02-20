#this code will calculate BMI with the help of user entered data.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_weight = float(weight)
new_height = float(height)
BMI = new_weight/(new_height**2)

#this will change change BMI type from float to int.
print(int(BMI))