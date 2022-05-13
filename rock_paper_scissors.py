import random 

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper or scissors?:").lower()

if player == computer:
    print("Computer's Turn: ", computer)
    print("Your's Turn:", player)
    print("You both Tie Match!")

elif player == "rock":
    if computer == "paper":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have loose this match!")

    if computer == "scissors":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have won this match!")

elif player == "paper":
    if computer == "scissors":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have loose this match!")

    if computer == "rock":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have won this match!")

elif player == "scissors":
    if computer == "rock":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have loose this match!")

    if computer == "paper":
        print("Computer's Turn:", computer)
        print("Yours Turn:", player)
        print("You have won this match!")


