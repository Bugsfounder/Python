import random

# SNAKE WATER GUN GAME
'''
ALL CASES:--
USER          COMP                  WIN                 WINNER
WATER   -     GUN         -->       WATER       -->      USER
SNAKE   -     WATER       -->       SNAKE       -->      USER
GUN     -     SNAKE       -->       GUN         -->      USER
GUN     -     WATER       -->       WATER       -->      COMP
WATER   -     SNAKE       -->       SNAKE       -->      COMP
SNAKE   -     GUN         -->       GUN         -->      COMP
'''


# FUNCTIONS

def checkUserInputIsNumericOrAlphabets(userInput):
    """
    HANDLING USER INPUT IF USER CHOOSE s, w, g or 1, 2, 3 checking user input is numeric or not if it is numeric than convert string numeric to integer else user choose alphabets like s, w, g than not convert to ingeter
    :param: userInput
    :globalVariable: using global variable using global keyword for userEnter var
    :return:  nothing
    """
    try:
        global userEnter
        if userInput.isnumeric():
            userEnter = int(userInput)
            # print(f"You enter {userEnter}")  # FOR DEBUGGING
        else:
            userEnter = userInput
            # print(f"You enter {userEnter}") # FOR DEBUGGING
    except Exception as error:
        print("Something went wrong Please Try again")
        # print("checking user choose 1 , 2, 3 or s, w, g")


def checkUserInputIsValidOrNot(userInput):
    """
    CHECKING IF USER INPUT IS NUMERIC THAN IT MUST BE GREATER THAN 0 OR LESS THAN OR EQUALS TO 3 OR IF USER INPUT IS NOT ISNUMERIC THAN IT MUST BE S, W, G NOTHING ELSE INSTEAD OF THIS
    :param userInput:
    :return: nothing
    """
    try:
        global userEnter
        if userInput.isnumeric():
            userEnter = int(userInput)
            # print("yes")
            # print(userEnter)
            if (userEnter <= 3) and (userEnter > 0):
                userEnter = userEnter
            else:
                print("Enter a valid Option nothing you choose instead 1, 2, 3")
        elif userInput == 's':
            userEnter = 1
            # print(f"you choose {userEnter}")
        elif userInput == 'w':
            userEnter = 2
            # print(f"you choose {userEnter}")
        elif userInput == 'g':
            userEnter = 3
            # print(f"you choose {userEnter}")
        else:
            print("Enter a valid Option nothing you choose instead s, w, g")
    except Exception as error:
        print("Something went wrong Please Try again")


def snakeWaterGunGame(userEnter, computerEnter, name):
    try:
        global userScore
        global compScore
        if ((userEnter == 1) and (computerEnter == 1)) or ((userEnter == 2) and (computerEnter == 2)) or (
                (userEnter == 3) and (computerEnter == 3)):
            print("Game Draw")
            print(f"{name} Enter {userEnter}")
            print(f"Computer Enter {computerEnter}")
        elif ((userEnter == 1) and (computerEnter == 2)) or ((userEnter == 2) and (computerEnter == 3)) or (
                (userEnter == 3) and (computerEnter == 1)):
            print(f"{name} Win")
            # print(f"{name} Enter {userEnter}")
            print(f"Computer Enter {computerEnter}")
            userScore += 1
        else:
            print(f"Computer Win")
            # print(f"{name} Enter {userEnter}")
            print(f"Computer Enter {computerEnter}")
            compScore += 1
    except Exception as error:
        print("Something went wrong Play again")


def scoreCalculate(userInput):
    if (userInput != 'q') or (userInput != 'p'):
        if userScore == compScore:
            print("Game Draw")
            print(f"Your Total Score is: {userScore}")
            print(f"Computer Total Score is: {compScore}")
        elif userScore > compScore:
            print(f"Congratulations! {name} You Wins This Game")
            print(f"Your Total Score is: {userScore}")
            print(f"Computer Total Score is: {compScore}")
        else:
            print(f"Computer Wins This Game")
            print(f"Computer Total Score is: {compScore}")
            print(f"Your Total Score is: {userScore}")


print("*****Welcome to Snake, Water, Gun Game*****")
name = input("Enter Your Name To Play: ")
i = 0

print(
    "Choose s for Snake, w for Water, g for Gun or you can use 1, 2, 3 as Snake, Water, Gun. Press q for quite, for leave one level press p, You have total 10 lives")
userScore = 0
compScore = 0
totalChances = 10
while i < 10:
    global userInput
    userInput = input(f"{name} Chance: ")
    computerEnter = random.randint(1, 3)  # SNAKE - 1, WATER - 2, GUN - 3
    # print(computerInput) # FOR DEBUGGING
    if userInput == 'q':
        break
    elif userInput == 'p':
        totalChances -= 1
        print(f"\t\t\t\t\t\t\t\t[Live:{totalChances}]")
        i += 1
        continue

    userEnter = userInput.lower()
    checkUserInputIsNumericOrAlphabets(userInput)
    checkUserInputIsValidOrNot(userInput)

    snakeWaterGunGame(userEnter, computerEnter, name)
    totalChances -= 1
    print(f"\t\t\t\t\t\t\t\t[Live:{totalChances}]")
    i += 1

scoreCalculate(userInput)
