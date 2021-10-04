grovery = ["Harpic", "Vim Bar", "Deodrant", "Bhindi", "Lollypop", "Chocolate"]

# WE CAN ADD ANY DATATYPE IN LIST
grovery = ["Harpic", "Vim Bar", "Deodrant", "Bhindi", "Lollypop", "Chocolate", 43, True]
# WE CAN ACCESS LIST ITEMS LIKE THIS:-
# print(grovery)
# print(grovery[0])  # ACCESS FIRST ELEMENT
# print(grovery[0:len(grovery):2])  # ACCESS FIRST ELEMENT

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [12, 43, 54, 23, 54, 87, 12, 65, 76, 65, 90]
# print(numbers)
# numbers.sort()
# numbers.reverse()
# print(numbers)
# print(numbers[3])
# print(numbers[0:11])
# print(numbers[:11])
# print(numbers[:])
# print(numbers[1:])
# print(numbers[1:4])
# print(numbers[::2])
# print(numbers[1:5:2])
# print(min(numbers))
# print(max(numbers))
# numbers.append(32)
# print(numbers)
# numbers.pop()
# numbers.insert(2, 1000)
# print(numbers)

# numbers[0] = 10
# print(numbers)

# MUTABLE --> values can be changed EX:- list
# INMUTABLE --> values cannot be changed EX:- tuple

# tp = (23, 43, 54, 12, 65)
# print(tp)
# print(tp[0])
# print(tp[0]) = 32 # --> error
# tp = (23,)  # single element tuple we have to add an extra comma
# print(tp)

# SWAPPING TWO NUMBERS
a = 32
b = 23
# TRADITIONAL WAY TO WAP TWO NUMBERS
# temp = a
# a = b
# b = temp

# SWAP USING PYTHON
a, b = b, a

print(a, b)
