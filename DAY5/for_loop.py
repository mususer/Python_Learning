# For Loop
# This code gives average of the heights entered by user.

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
 
sum = 0
num = 0

for i in student_heights:
    sum = sum + student_heights[num]
    num = num + 1
    
print(sum)
print(num)
avg = round(sum/num)
print(avg)