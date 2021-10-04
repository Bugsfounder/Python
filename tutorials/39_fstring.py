# F-Strings & String Formatting In Python | Python Tutorials For Absolute Beginners In Hindi #39

# me = "Manisha"
# a = "This is %s" % me
# print(a)
# print("age %d" % 3)

# me = "Manisha"
# a1 = 23
# a = "This is %s %d" % (me, a1)
# print(a)
# print("age %d" % 3)


me = "Manisha"
a1 = 23
# a = "This is {} {}"
# a = "This is {0} {1}"
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
# print("age %d" % 3)

a = f"This is {me} {a1} {2 * 5}"
print(a)
