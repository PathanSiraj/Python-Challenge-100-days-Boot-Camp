import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user=int(input('you have choices 0 for rock ,1 for paper ,2 for scissors choose any one:'))
if user<=2 and user>0:
    print(user)
    print(game_images[user])
    computer = random.randint(0, 2)
    print(f'computer choose:{computer}')
    print(game_images[computer])
    if user==0 and computer==2:
        print('you win the game')
    elif user==2 and computer==0:
        print("you loose computer win!")
    elif user>computer:
        print('you win the game')
    elif computer>user:
        print("you loose computer win!")
    else:
        print('the game is draw!')

else:
    print('invalid option.you loose')
