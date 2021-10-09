# PYTHON PRACTICE PROBLEM 3 (EASY, 15 POINTS)
# Foods and Calories

# You visit a restaurant called CodeWithHarry and food items in this restaurant are sorted based on their amount of calories. You have to reverse this list of food items and their calories.


# You have to use following three methods to reverse a list:
# • Inbuilt method of python
# • Lastname[::-1] slicing trick
# • Swapping first element with last one and second element with second las one and so on...


# Input:
# Take a list as an input from user
# [5,4,2]

# Output:
# [1,4,5]
# [1,4,5]
# [1,4,5]

# All three methods gives same result


userInput = input("Enter list items with comma separate: ")

lst = userInput.split(",")


def revUsingInBuilt(lst):
    lst.reverse()
    print(lst)


def revUsingSliceTrick(lst):
    print(lst[::-1])


def revUsingSwap(lst):
    first = 0
    last = len(lst) - 1

    while first < last:
        temp = lst[first]
        lst[first] = lst[last]
        lst[last] = temp
        first += 1
        last -= 1

    print(lst)


reverse1 = lst[:]
reverse2 = lst[:]
reverese = lst[:]
reverese3 = lst[:]

for i in range(len(reverese) // 2):
    reverese[i], reverese[len(reverese) - i - 1] = reverese[len(reverese) - i - 1], reverese[i]
print(reverese)

revUsingInBuilt(reverse1)
revUsingSliceTrick(reverse2)
revUsingSwap(reverese3)
