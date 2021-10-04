# list1 = ["Manisha", "Harry", "Larry", "Carry", "SkillF"]
# list1 = ("Manisha", "Harry", "Larry", "Carry", "SkillF")
# list1 = [["Manisha", 1], ["Harry", 1], ["Larry", 10], ["Carry", 0], ["SkillF", 3]]

# dic = dict(list1)
# print(dic)

# for item, lollypop in list1:
#     print(item, lollypop)

# for item, lollypop in dic.items():
#     print(item, lollypop)

# myDict = {
#     "name": "Manisha",
#     "age": 17,
#     "class": "Bsc"
# }
# for key in myDict:
# print(key)
# print(key)
# print(key, "=", myDict.get(key))


# QUICK QUIZ:- WRITE A PYTHON PROGRAM TO PRINT LIST ITEMS IF ITEM IS A NUMBER OR GREATER THAN 6

myList = [1, 4, "this", 89, 43, 2, 54, 6, "There", "Harry", "manisha", 7, 8, 9, int, float, False]
for item in myList:
    if str(item).isnumeric() and item >= 6:
        print(item)
