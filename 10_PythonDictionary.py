# DICTIONARY IS NOTHING BUT KEY VALUE PAIRS
d1 = {}
# print(type(d1))
dict1 = {
    "apple": "seb",
    "Girl": "Ladki",
    "Boy": "Ladka",
    "myDict": {"banana": "kela", "computer": "operating machine"}
}
# dict1['book'] = "kitab"
# print(dict1["apple"])
# print(dict1["Girl"])
# print(dict1["Boy"])
# print(dict1["myDict"]["banana"])
# print(dict1["myDict"]["computer"])
# print(dict1["book"])
# del (dict1['book'])
print(dict1)
dict2 = dict1.copy()
dict2['New'] = "Naya"
print(dict2)
print(dict2.items())
