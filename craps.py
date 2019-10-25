# Olivia Lee
# 10-21-19
# Dice game with betting.
# Due Friday 10-25-19

import random


def rollDice():
    roll = random.randint(2, 12)
    return roll


# What is the total amount the player has to bet?
def create():
    total = int(input("Please enter the total amount you will be betting from today:"))
    return total


def playGame():
    bet = int(input("Please enter your bet:"))
    while bet <= 0:
        print("Your bet is less than or equal to zero. Please enter a new bet:")
        bet = int(input())
    while total > 0 and bet > 0 and bet <= total:
        print("You rolled a " + str(roll))
        if roll == 2 or roll == 3 or roll == 12:
            print("You rolled either a 2, 3 or a 12, you lose.")
            start_total = start_total - bet
        elif roll == 7 or roll == 11:
            print("You rolled a 7 or an 11, you win!")
            start_total = start_total + bet
        else:
            roll2 = rollDice()
            if roll2 == roll:
                print("You win!")
                start_total = start_total + bet
            elif roll2 == 7:
                print("Sorry, you lose.")
                start_total = start_total - bet
            else:
                print("new roll")
                roll3 = rollDice()


total = create()
roll = rollDice()
start_total = total
playGame()
