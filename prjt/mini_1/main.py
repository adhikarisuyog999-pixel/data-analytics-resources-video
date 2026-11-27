
import random

def computerinput():
    randomno = random.randint(1, 3)

    if randomno == 1:
        return "rock"
    elif randomno == 2:
        return "scissors"
    else:
        return "paper"


def userinput():
    try:
        user = int(input("Your turn (1: Rock, 2: Scissors, 3: Paper): "))

        if user == 1:
            return "rock"
        elif user == 2:
            return "scissors"
        elif user == 3:
            return "paper"
        else:
            print("Invalid input!")
            return userinput()

    except ValueError:
        print("Please enter a number!")
        return userinput()


def game_winner(user, computer):

    if user == computer:
        return "It's a draw!"

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"

    else:
        return "Computer wins!"


# MAIN MENU
while True:

    print("\n--- Rock Paper Scissors ---")
    print("1. Play")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Thanks for playing!")
        break

    elif choice == "1":

        print("\nComputer is ready!")

        user = userinput()
        computer = computerinput()

        print("\nYou chose:", user)
        print("Computer chose:", computer)

        result = game_winner(user, computer)

        print(result)

    else:
        print("Invalid choice!")
