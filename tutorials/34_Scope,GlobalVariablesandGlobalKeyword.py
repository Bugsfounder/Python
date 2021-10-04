# l = 10  # GLOBAL VARIABLE
# def function1(n):
#     # l = 5  # LOCAL VARIABLE
#     global l
#     l = l + 32
#     m = 8  # LOCAL VARIABLE
#     print(l, m)
#     print(n, "I have Printed")
# function1("This is me")
# # print(m)
# print(l)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 8

    # print("Before Calling rohan", x)
    rohan()
    print("After Calling rohan", x)


harry()
print(x)
