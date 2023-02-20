# This code contains nested list concept
# It will allows you to mark a square on the map using a two-digit system.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
#nested list
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row = int(position[1]) - 1
col = int(position[0]) -1
map[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}")





