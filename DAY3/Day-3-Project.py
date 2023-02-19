print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("######### Welcome to Treasure Island Game ###########")
print(" ")
print("Your mission is to find the treasure.")
print("You are at cross-roads, where you want to go?")
choose = input("Type left or right? :")
if choose == "left":
  print(" ")
  print("You are at corner of the sea, what would you choose? swim the lake or wait for the boat.")
  choose2 = input("Type swim or wait? :")
  if choose2 == "wait":
    print(" ")
    print("You crossed the sea!!! Now you have three doors of luck, which color door would you choose ? ")
    choose3 = input( "Type red or blue or yellow? :")
    if choose3 == "yellow":
      print(" ")
      print("Hurray You win!!!")
    elif choose3 == "blue":
      print(" ")
      print("Eaten by beasts.")
      print("Game Over.")
    elif choose3 == "red":
      print(" ")
      print("Burned by fire.")
      print("Game Over.")
    else:
      print(" ")
      print("Game Over.")
  else:
    print(" ")
    print("Attached by trout.")
    print("Game Over.")
else:
  print(" ")
  print("Fall into a hole.")
  print("Game Over.")
    
    


