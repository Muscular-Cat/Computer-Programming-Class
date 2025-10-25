import random


def getUWeapon():
    print("\nSELECT YOUR WEAPON (1-3)")
    print("------------------------")
    print("1. Rock\n2. Paper\n3. Scissors")
    return int(input("Enter your weapon: "))


def getOWeapon():
    return random.randrange(1, 4)


def getWinner(user, opp):
    print(f"You: {user} - Opponent: {opp}")
    if (user == opp):
        print("It's a tie!")
    elif (user == 1 and opp == 3) or (user == 2 and opp == 1) or (user == 3 and opp == 2):
        print("You win!")
    else:
        print("You lose!")


def main():


    while True:
        getWinner(getUWeapon(), getOWeapon())


        if (input("Want to play again (y/n):") != "y"):
            break


if __name__ == "__main__":


    main()
    print("Completed by, Teage Blanton")
