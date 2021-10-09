# PYTHON PRACTICE PROBLEM 5 (15 POINTS)
# Palindromify The List

# You have given a list which contains some numbers, You have to print a list of next
# palindromes if the numbers is greater than 10 otherwise you will print that number.

# Input:
# [1, 6, 87, 43]

# Output:
# [1, 6, 88, 44]


"""
Author: Manisha
Date: 09/10/2021
Purpose: Python Practice
"""


# CREATING A FUNCTION THAT THAT REVERSE A NUMBER EX:- 21 TO 12
def reverse(num):
    """
    THIS FUNCITON REVERSE A NUMBER
    :param num:
    :return: REVERSED NUMBER
    """
    val = str(num)[::-1]
    return int(val)


# CREATING A FUNCTION THAT RETURNS NEXT PALINDROME A NUMBER IF THAT NUMBER IS LESS THAN 10 THAN RETURN THAT NUMBER AS IT IS
def isPalindrome(num):
    """
    THIS FUNCTION IS RETURN NEXT PALINDROME OF A NUMEBR IF NUMBER IS LESS THAN 10 THAN RETURN THAT NUMBER AS IT IS
    :param num:
    :return: NEXT PALINDROME NUMBER OF NUM
    """
    number = num
    while True:
        number += 1
        if num < 10:
            return num
        elif number == reverse(number):
            return number


try:
    nOfNum = int(input("How many number's palindrome do you want to take: "))
    # TAKING INPUT FORM USER IN USERINPUTS LIST USING LIST COMPREHENSION
    userInputs = [int(input(f"Enter Number {i + 1}: ")) for i in range(nOfNum)]
    # APPENDING PALINDROMIC NUMBERS TO PALINDROMIC LIST USING LIST COMPREHENSION
    palindromic = [isPalindrome(userInputs[i]) for i in range(len(userInputs)) if isPalindrome(userInputs[i]) != None]
    print(palindromic)
except Exception as e:
    print("Something went wrong check inputs correctly only integers are allowed")
