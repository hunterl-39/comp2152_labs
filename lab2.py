choices = ["Rock", "Paper", "Scissors"]

playerChoice = int(input("Enter your choice:1=Rock, 2=Paper, 3=Scissors"))

if playerChoice < 1 or playerChoice > 3:
    print("Error choose between 1 and 3.")
else:
    computerChoice = int(input("Enter computer choice: 1=Rock, 2=Paper, 3=Scissors"))

    if computerChoice < 1 or computerChoice > 3:
        print("Error Choose between 1 and 3.")
    else:
        player = choices[playerChoice - 1]
        computer = choices[computerChoice - 1]

        print("Player chose:", player)
        print("Computer chose:", computer)

        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors so You win")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock so You win")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper so You win")
        else:
            print("You lose!")

        if player != "Rock":
            print("You didn't pick the classic Rock...")