# ls = []
# for i in range(100):
#     if (i % 3 == 0):
#         ls.append(i)
# print(ls)

# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)
j = 2
# dict1 = {i: f"item{i}" for i in range(1, 10001) if i % 100 == 0}
# dict1 = {i: f"Item{i}" for i in range(5)}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict1)
# print(dict2)

# dresses = {dress for dress in
#            ["Dress1", "Dress2", "Dress1", "Dress2", "Dress1", "Dress2", "Dress1", "Dress2", "Dress1", "Dress2",
#             "Dress1", "Dress2", "Dress1", "Dress2",
#             "Dress1", "Dress2", ]}

# print(dresses)
# print(type(dresses))

# evens = (i for i in range(100) if i % 2 == 0)

# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# for item in evens:
#     print(item)

# QUICK QUIZ:-

userlist = input("Enter Your List divide by ,: ")
t = int(
    input(
        "Which type of comprehension you use:- \n1. List Comprehension \n2.Dictionary Comprehension \n3. Set Comprehension\n "))
list = userlist.split(",")
# print(list)

if t == 1:
    item = [list[i] for i in range(len(list))]

elif t == 2:
    item = {i: f"{list[i]}" for i in range(len(list))}
elif t == 3:
    item = {i for i in list}
else:
    print("select valid option")

print(item)
