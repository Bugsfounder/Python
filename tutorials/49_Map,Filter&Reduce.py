# *******************MAP*******************
# number = ["32", "543", "90"]
# numbers = list(map(int, number))

# for i in range(len(number)):
#     number[i] = int(number[i])
# def sq(a):
#     return a * a

# num = [2, 4, 6, 3, 5, 67]

# square = list(map(sq, num))
# square = list(map(lambda x: x * x, num))
#
# print(square)

# def square(a):
#     return a * a

# def cube(a):
#     return a * a * a

# funcs = [square, cube]
# num = [2, 4, 6, 3, 5, 67]

# for i in range(5):
#     val = list(map(lambda x: x(i), funcs))
#     print(val)


# *******************FILTER*******************
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def isGreater5(num):
#     return num > 5
# grThan5 = list(filter(isGreater5, list1))
# print(grThan5)

# *******************REDUCE*******************

from functools import reduce

list = [1, 2, 3, 4, 5, 6, 9]
# num = reduce(lambda x, y: x + y, list)
num = reduce(lambda x, y: x * y, list)
# num = 0
# for item in list:
#     num += item
# print(num)
print(num)
