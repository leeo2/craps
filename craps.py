# Olivia Lee
# 10-21-19
# Dice game with betting.
# Due Friday 10-25-19

import random


# Roll two dice
def rollDice():
    roll = random.randint(2, 12)
    return roll


# What is the total amount the player has to bet?
def create():
    total = int(input("Please enter the total amount you will be betting from today: "))
    return total


def playGame():
    start_total = create()
    choice = 1
    while choice == 1:
        if start_total == 0:
            print("You are out of money. Game over")
            choice = 0
        else:
            bet = int(input("Please enter your bet: "))
            if bet > start_total:
                print("Invalid bet")
            else:
                roll = rollDice()

                while bet <= 0:
                    print("Your bet is less than or equal to zero. Please enter a new bet: ")
                    bet = int(input())
                print("You rolled a " + str(roll))
                if roll == 2 or roll == 3 or roll == 12:
                    print("You rolled either a 2, 3 or a 12, you lose.")
                    start_total = start_total - bet
                    print(f"Balance remaining: {start_total}")
                elif roll == 7 or roll == 11:
                    print("You rolled a 7 or an 11, you win!")
                    start_total = start_total + bet
                    print(f"Balance remaining: {start_total}")
                else:
                    roll2 = rollDice()
                    print(f"roll 2 = {roll2}")
                    while roll2 != roll and roll2 != 7:
                        roll2 = rollDice()
                        print(f"roll 2 = {roll2}")
                    if roll2 == roll:
                        print("You win!")
                        start_total = start_total + bet
                        print(f"Balance remaining: {start_total}")
                    elif roll2 == 7:
                        print("Sorry, you lose.")
                        start_total = start_total - bet
                        print(f"Balance remaining: {start_total}")

    print("Would you like to play again?  1 for yes.")
    choice = int(input())
    if choice == 1:
        playGame()



roll = rollDice()
playGame()

