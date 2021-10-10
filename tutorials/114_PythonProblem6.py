# PYTHON PRACTICE PROBLEM 6 (EASY, 15 POINTS)
# Problem Statement:-
# Generate a random integer from a to b. You and your friends have to guess a number between two numbers, a and
# b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep
# choosing the number, and your program must tell whether the number is greater than the actual number or less
# than the actual number. Log the number of trials it took your friend to arrive at the number. You play the
# same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking
# a and b as input and don’t show that to the user.
#
# Input:
# Enter the value of a
#
# 4
#
# Enter the value of b
#
# 13
#
# Output:
# Player1 :
#
# Please guess the number between 4 and 13
#
# 5
#
# Wrong guess a greater number again
#
# 8
#
# Wrong guess a smaller number again
#
# 6
#
# Correct, you took 3 trials to guess the number
#
# Player 2:
#
# Correct, you took 7 trials to guess the number
#
# Player 1 wins!


"""
Author: Manisha
Date: 09/10/2021
Purpose: Python Practice
"""

import random


# CREATING A WINNER FUNCTION THAT TAKE LIST OF NUMBERS AND RETURN WHICH NUMBERS IS LOWER
def winner(numOfList):
    great = numOfList[0]
    for i in range(len(numOfList)):
        if numOfList[i] == great:
            great = great
        elif numOfList[i] < great:
            great = numOfList[i]
    return great


# CREATING A WHOWIN FUNCTION THAT HANDLE MOST OF OUR GAME FUNCTIONALITY
def whoWin(namesOfPlayer, start, end):
    usersScoreDict = {}
    usersScoreList = []
    winners = []
    for i in range(len(namesOfPlayer)):
        playerScore = 1
        computerGuess = random.randint(start, end)
        print(f"\n\t\t[PLAYER: {namesOfPlayer[i].upper()}]\n")
        while True:
            playerGuess = int(input(f"Please Guess The Number Between {start} and {end}: "))
            if playerGuess < start or playerGuess > end:
                print(f"Enter Number Between {start} and {end}")
            elif playerGuess > computerGuess:
                print(f"Lower Number Please!")
                playerScore += 1
            elif playerGuess < computerGuess:
                print(f"Greater Number Please!")
                playerScore += 1
            elif playerGuess == computerGuess:
                print(f"Correct Guess, You Took {playerScore} Trials to Guess The Number")
                break
            else:
                break
        usersScoreDict[playerScore] = namesOfPlayer[i]
        usersScoreList.append(playerScore)
    win = winner(usersScoreList)
    print(f"\n\t\t[WINNER: {usersScoreDict[win].upper()}]")


# HERE IS OUR MAIN FUNCTION
if __name__ == '__main__':
    print("******* Welcome to Number Guessing Game *******")
    try:
        start = int(input("Enter Minimum Number from You want Guess: "))
        end = int(input("Enter Minimum Number where You want Guess: "))
        numOfPlayers = int(input("How Many Players want To Play the Game: "))
        namesOfPlayer = [input(f"Enter Player {i + 1} Name: ") for i in range(numOfPlayers)]

        whoWin(namesOfPlayer, start, end)
    except Exception as error:
        print("Only Numbers are Allowed")
