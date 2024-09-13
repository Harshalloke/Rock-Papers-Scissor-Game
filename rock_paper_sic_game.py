import random
option=("rock","paper","scissor")

while True:
    computer=random.choice(option)
    player=input("Enter the choice from 'rock,paper,scissor' :")
    if player not in option:
        player=input("Enter the choice from 'rock,paper,scissor' :")
    else:
        print(f"You Chosed :{player}")
        print(f"Computer Chosed :{computer}")
        if player=="rock" and computer=="scissor":
            print("YOU WIN !!")
        elif player=="paper"and computer=="rock":
            print("YOU WIN !!")
        elif player=="scissor"and computer=="paper":
            print("YOU WIN !!")
        elif player==computer:
            print("IT's an TIE !!")
        else:
            print("YOU LOST !!")

        restart=input("Do you want to play it again type(y/n):").lower()
        if restart =="n":
            print("Thank You for Playing")
            break

