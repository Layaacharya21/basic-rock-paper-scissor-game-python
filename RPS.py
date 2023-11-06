import random

while True:
    choice=input("Choose rock,paper,scissors ").lower()
    choices=["rock","paper","scissors"]
    comp_choice=random.choice(choices)

    if choice==comp_choice:
        print("Its a tie")
    elif(
        (choice=="rock" and comp_choice=="scissors") or
        (choice=="paper" and comp_choice=="rock") or
        (choice=="scissors" and comp_choice=="paper")
        ):
        result="YOU WIN"
    else:
        result="computer won"
    print("Player choice: ",choice)
    print("Computer choice: ",comp_choice)
    print(result)

    a=input("Do you want to play again?").lower()
    if a!="yes":
        break 
