print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('you\'re here to find tressure youchoose the paths either "left" or "right"?').lower()
if choice1=="left":
    choice2=input('you\'re in a pond you swim or "wait" for "boat"?').lower()
    if choice2=="wait":
        choice3=input('you will reach the island in front three doors what will you choose"red"or"yellow"or"blue"?').lower()
        if choice3=="red":
            print('there are flames game over')
        elif choice3=="yellow":
            print('you win tressure is your\'s')
        elif choice3=="blue":
            print('there is sea beasts you\'re over')
        else:
            print("invalid")
    elif choice2=="swim":
        print('there is sharks game over')
    else:
        print('invalid')
elif choice1=="right":
    print('ther is hole game over')
else:
    print('invalid')