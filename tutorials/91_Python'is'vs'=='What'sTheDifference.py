# == - value equality - Two objects have the same value
# is - reference equality - Two references refers to the same object
# b = a
# a ==b
# True
# b is a
# True
# b[0] = 0
# a
# [0, 2, 3]
# c = a[:]
# c
# [0, 2, 3]
# a==c
# True
# a is c
# False

# Task:

a = [6, 4, "34"]
b = [6, 4, "34"]
print(b is a)  # FALSE BECAUSE B IS NOT REFERS TO A OR A IS NOT REFERS TO B BOTH ARE TWO DIFFERENT OBJECTS
print(b == a)  # TRUE BECAUSE BOTH OBJECTS HAS SAME VALUE
