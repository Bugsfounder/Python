s = set()  # EMPTY SET
# print(type(s))
# sets = {32, 54, 65, 23, 5, 34, 32}
# print(sets)

# s_from_list = set([1, 2, 3, 4, 5, 6, 2])
# print(s_from_list)

s.add(1)
s.add(1)
s.add(2)

# s1 = s.union({1, 2, 3, 4})
s1 = s.intersection({1, 2, 3, 4})
print(s, s1)
print(len(s))
print(min(s1))
print(max(s1))

s1 = {5, 6}
print(s.isdisjoint(s1))
s.remove(2)
print(s)
