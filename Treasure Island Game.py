print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("welcome to treasure island,")
print("your mission is to find the treasure,")
choice_1=input('you\'re at a crossroad,where do'
               'you want to go? type "left"or"right".').lower()
if choice_1=="left":
    choice_2=input('you\'ve comr to a lake.'
                   'there is an island in the middle of the lake.'
                   'type"wait"to wait for a boat.'
                   'type"swim"to swim across.').lower()
    if choice_2=="wait":
        choice_3=input("you arrive at the iseland unharmed."
                   "there is house with 3 doors.one red,"
                   "one tellow and one blue."
                   "which colour room do you choose?").lower()
        if choice_3=="red":
            print("it's a eoom full of fire. Game over")
        elif choice_3=="yellow":
            print("you found the treasue.you win!")
        elif choice_3=="blue":
            print("you enter a room of beasts. Game over.")
        else:
            print("door nevr exist pleas enter the corect door colour")
    else:
        print("you got attacked by an anger trout.Game is over.")
else:
    print("you fell in to a hole.Game Over.")     
