# 5*4*3*2*1
# n*n-1 * n-2 * n-3 * n-4.........1
# n! = n * (n-1)!

def factorial_iterative(n):
    """
    :param n: INTEGER
    :return: n*n-1 * n-2 * n-3 * n-4.........1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def factorial_recursive(n):
    """
    :param n: INTEGER
    :return: n*n-1 * n-2 * n-3 * n-4.........1
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
        # 5 * factorial_recursive(4)
        # 5 * 4 * factorial_recursive(3)
        # 5 * 4 * 3 * factorial_recursive(2)
        # 5 * 4 * 3 * 2 * factorial_recursive(1)
        # 5 * 4 * 3 * 2 * 1 = 120


# 0 1 1 2 3 5 8 13
# number = int(input("Enter a Number: "))
# print("Factorial using iterative method:", factorial_iterative(number))
# print("Factorial using Recursive method:", factorial_iterative(number))


# QUICK QUIZ: CREATE A FUNCTION TO CALCULTE FIBONACCI SERIES

def fibSeries(n):
    if n <= 1:
        return n
    else:
        return fibSeries(n - 1) + fibSeries(n - 2)


number = int(input("Enter a Number: "))
for i in range(number):
    print(fibSeries(i))
