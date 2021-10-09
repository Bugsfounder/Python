"""
Author: Manisha
Date: 09/10/2021
Purpose: Practice Problem of Python
"""


# PYTHON PRACTICE PROBLEM 4 (15 POINTS)
# The Next Palindrome

# A palindrome is a string which when reversed is equal to itself:
# Examples of palindrome include 616, mom, 676, 10000001

# You have to take a number as input form the user. You have to find out next palindrome corresponding to that number.
# Your first input should be number of text cased and then take all the cases as input from the user

# Input:
# 3
# 451
# 10
# 2133
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2133 is 2222

#

def reverse(num):
    n = str(num)
    rev = n[::-1]
    return int(rev)


try:
    nOfNum = int(input("How many number's palindrome do you want to take: "))

    i = 0
    userInputs = []
    while i < nOfNum:
        userInputs.append(int(input(f"Enter Number {i + 1}: ")))
        i += 1

    for i in range(len(userInputs)):
        item = userInputs[i]
        while True:
            userInputs[i] += 1
            if userInputs[i] == reverse(userInputs[i]):
                print(f"Next Palindrome for {item} is {userInputs[i]}")
                break
except Exception as e:
    print("Something went wrong check inputs correctly only integers are allowed")
