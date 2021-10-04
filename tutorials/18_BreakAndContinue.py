# i = 0
# while True:
#     i += 1
#     if i + 1 < 5:
#         continue
#
#     print(i + 1, end=" ")
#     if i == 40:
#         i += 1
#         break  # stop the loop
#
#     i += 1


# QUICK QUIZ:- CONTINUE TAKING INPUT FROM USER WHILE USER INPUT IS NOT GREATER THAN 100

i = 0
con = True;

while con:
    userInput = int(input("Enter a Number: "))
    if (userInput < 100):
        print("Enter a greater number")
        continue
    else:
        print("Superb Number")
        con = False
        break;
