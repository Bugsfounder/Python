# PATTERN PRINTING
"""
TAKE INPUT - INTEGER N AND PRINT THE PATTERN BELOW
TAKE INPUT BOOLEAN - TAKE INPUT AS 0 OR 1 AND TYPECAST TO BOOLEAN TRUE/FALSE

IF TRUE ASSUME N = 4 HERE
*
* *
* * *
* * * *

IF FALSE ASSUME  N = 4 HERE
* * * *
* * *
* *
*
"""

numOfRow = int(input("Enter the Number of row: "))
incAndDec = int(input("Enter 0 for print start in decreasing order and 1 for increasing order: "))

if incAndDec:
    for i in range(0, numOfRow):
        for j in range(0, i + 1):
            print("*", end=" ")

        print("\r")
else:
    for i in range(numOfRow + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=" ")

        print("\r")
