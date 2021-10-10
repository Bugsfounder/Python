# PYTHON PRACTICE PROBLEM 8 (MEDIUM, 20 POINTS)
# Jumbled Funny Names

# Problem Statement:-
# It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.

# Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

# Input:
# Enter number of friends:

# 3

# Enter the name of your 3 friends:

# Rohan Das

# Shubham Agarwal

# Ritesh Arora

# Output:

# Ritesh Das

# Shubham Arora

# Rohan Agarwal

import random


def swapNames(listOfNames):
    allSplitedNames = []
    for i in range(len(listOfNames)):
        allSplitedNames.append(listOfNames[i].split(" "))

    for i in range(len(allSplitedNames)):
        randi = random.randint(0, len(allSplitedNames) - 1)
        for j in range(len(allSplitedNames)):
            allSplitedNames[i][1] = allSplitedNames[randi][1]

    return allSplitedNames


# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += f"{ele} "

        # return string
    return str1


if __name__ == '__main__':
    print("******** Jumbled Funny Names ********")
    numOfFriends = int(input("How Many Name do You want to Jumbled: "))

    usersFriendsList = []

    for i in range(numOfFriends):
        usersFriendsList.append(input(f"Enter Name of Friend {i + 1}: ").capitalize())

    jumbledName = swapNames(usersFriendsList)

    for i in range(len(jumbledName)):
        name = listToString(jumbledName[i])
        print(name)

# import random
#
# t = int(input("Enter the number of names you want to input\n"))
# names = []
# for i in range(t):
#     names.append(list(input().split(" ")))
# for i in range(t):
#     print(names[i][0] + " " + names[random.randint(i, t - 1)][random.randint(1, len(names[i]) - 1)])
