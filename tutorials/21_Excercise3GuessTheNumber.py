# NUMBER OF GUESSES 9
# PRINT NUMBER OF GUESSES LEFT
# GAME OVER

number = 18
totalNumberOfGuesses = 9
wrongGuess = True

print("You have", totalNumberOfGuesses, "chance to guess")
userGuess = int(input("Guess a Number: "))

while wrongGuess:
    totalNumberOfGuesses -= 1
    userGuess = int(input("Guess a Number: "))
    if userGuess == number:
        print("You Guess the Correct Number in ", totalNumberOfGuesses, "Guess")
        print("Congratulations! You Guess The Correct Number")
        break
    elif totalNumberOfGuesses == 0:
        print("Game Over")
        break
    elif userGuess > number:
        print("You have", totalNumberOfGuesses, "chance to guess")
        print("Lesser Number Please")
    else:
        print("You have", totalNumberOfGuesses, "chance to guess")
        print("Greater Number Please")
