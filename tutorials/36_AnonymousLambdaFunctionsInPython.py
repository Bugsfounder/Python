# Anonymous/Lambda Functions In Python
# def add(a, b):
#     return a + b
# minus = lambda a, b: a - b
# print(minus(9, 5))

# def a_first(a):
#     return a[1]


a = [[1, 43], [76, 6], [0, 9]]
# a.sort(key=a_first)
a.sort(key=lambda x: x[1])

print(a)
