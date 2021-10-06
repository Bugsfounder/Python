"""
ITERABLE - __iter__() or __getitem__()
ITERATOR - __next__()
ITERATION
"""


# for i in range(80):
#     print(i)


def gen(n):
    for i in range(n):
        yield i


g = gen(10)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for g in g:
#     print(g)

manisha = "Manisha"

# manisha.__iter__()
# manisha.__getitem__()
iter = iter(manisha)
print(iter.__next__())

# for char in manisha:
#     print(char)
