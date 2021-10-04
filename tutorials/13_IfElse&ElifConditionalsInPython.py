# var1 = 5
# var2 = 6
# var3 = int(input("Enter a Number: "))
#
# if var3 > var1:
#     print(var3, " is Greater")
# # if var3 == var1:
# #     print(var3, " is Equal")
# elif var3 == var1:
#     print(var3, " is Equal")
# else:
#     print(var3, " is Less than")
#
# # if var3 > var1:
# #     print(var3, " is Greater Than ", var1)
# # elif var3 > var2:
# #     print(var3, " is Greater Than ", var2)
# # else:
# #     print(var3, " is Less than all variables")

# lst = [3, 2, 5, 2, 6]
# print(5 in lst)
# print(50 in lst)
#
# print(5 not in lst)
# print(50 not in lst)
# if 5 in lst:
#     print("Yes, its in the list")


# QUICK QUIZE:- TAKE INPUT FROM USER AS AGE IF AGE > 18 THAN YOU CAN DRIVE ELSE NOT IF AGE == 18 WE CAN'T DECIDE
age = int(input("Enter Your age: "))
if age > 18:
    print("Congratulations! You can drive")
elif age == 18:
    print("Sorry, We can't decide or You have to wait for one Year")
else:
    print("Sorry, You cannot Drive")
