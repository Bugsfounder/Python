import json

# json.load() and json.loads()
data = '{"name":"Manisha", "age":17}'
print(data)
# print(data['name'])
parsed = json.loads(data)

print(parsed)
print(parsed['name'])
print(type(parsed))

# TASK-1 : json.load()?
# json.load is use for read a json file json.loads() is use to parse string json to python dictionary


# json.dump() and json.dumps()
data2 = {
    "chennal_name": "Manisha",
    "cars": ["BMW", "audi 8A", "ferrari"],
    "fridge": ("roti", "biri 540", 88),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task-2: what is sort_keys parameter in dump
formatted = json.dumps(data2, indent=4, sort_keys=True)
print(formatted)
