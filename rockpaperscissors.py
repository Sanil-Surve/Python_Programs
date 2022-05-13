import random

print("Winning Rules of the Rock paper scissor game as follows: \n" + "Rock vs paper -> paper wins \n" + "Rock vs scissors -> Rock wins \n" + "scissors vs paper -> scissors wins \n")

while True:
    print("Enter choice  \n 1 for Rock, \n 2  for paper,\n 3 for scissors \n")

    choice = int(input("User turn: "))

    while choice > 3  or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        choice_name = "Rock"
                     
    elif choice == 2:
        choice_name = "Paper"

    else:
        choice_name = "Scissors"

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice_name = random.randint(1,3)
