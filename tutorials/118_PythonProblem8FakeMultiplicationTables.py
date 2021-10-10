# PYTHON PRACTICE PROBLEM 8 (MEDIUM, 20 POINTS)
# Fake Multiplication Tables

# Problem Statement:-
#  Rohan das is a fraud by nature. Rohan Das wrote a python function to print a
#  multiplication table of a given number and put one of the values (randomly
#  generated) as wrong.

# Rohan Das did this to fool his classmates and make them commit a mistake in a test.
# You cannot tolerate this!

# So you decided to use your python skills to counter Rohan’s actions by writing a
# python program that validates Rohan’s multiplication table.

# Your function should be able to find out the wrong values in Rohan’s table and
# expose Rohan Das as a fraud.

# Note: Rohan’s function returns a list of numbers like this

# Rohan Das’s Function Input:
# rohanMultiplication(6)

# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]

# You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None

import random


def fakeMultiplicationTable(tableOf):
    table = []
    randomIndex = random.randint(2, 8)
    for i in range(10):
        table.append(tableOf * (i + 1))
        if randomIndex == i:
            table[i] = tableOf * (randomIndex * 2)

    return table


def checkTableIsCorrect(lst, tableOf):
    wrongTable = lst
    correctTable = []
    for i in range(len(lst)):
        correctTable.append(tableOf * (i + 1))

    for i in range(len(correctTable)):
        wrongIndex = 0
        if correctTable[i] != wrongTable[i]:
            wrongIndex = i
            return f"The Table is Wrong on {i} index. It is {wrongTable[i]} but it must be has {correctTable[i]}"


if __name__ == '__main__':
    wt = fakeMultiplicationTable(6)
    ct = checkTableIsCorrect(wt, 6)
    print(wt)
    print(ct)
