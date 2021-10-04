lis = ["John", "cena", "Randy", "Orton", "Sheamus", "Khali", "Jinder Mahal"]

# for item in lis:
#     print(item, "and ", end="")

# a = " and ".join(lis)
# a = ", ".join(lis)
# print(a)

# Python program to print list
# using for loop
# a = [1, 2, 3, 4, 5]


# printing the list using loop
list = ["John", "cena", "Randy", "Orton", "Sheamus", "Khali", "Jinder Mahal"]


def myJoin(list, join):
    for x in range(len(list)):
        if x <= len(list) - 1:
            print(list[x], end="")
        if x != len(list) - 1:
            print(join, end="")


myJoin(lis, " and ")
