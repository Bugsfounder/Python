# a = 43
# b = 89
# c = sum((a, b))  # BUILT IN FUNCTION
# print(c)


# USER DEFINED FUNCTIONS
# def function1():
#     print("Hello You are in Function")

# function1()  # FUNCTION CALL


# FUNCTION CAN TAKE PARAMETERS
# def func1(a, b):
#     print("Hello You are in Function", a + b)

# func1(12, 43)

# FUNCTION CAN BE RETURN SOMETHING
# def func2(a, b):
#     """This is the function which will calculate average of two numbers"""
#     return (a + b) / 2
#
#
# avg = func2(12, 32);
# print(avg)


def func3(a, b):
    """Inside any function if you put comment on first line this is called docstring you can get the docstring from the outside of the function as a function call like:- func3.__doc__ note that no parentheses.
    This is the function which will calculate average of two numbers this function doesn't work for three numbers"""
    return (a + b) / 2


# avg = func3(12, 32)
docStr = func3.__doc__
docStr = print.__doc__
print(docStr)
