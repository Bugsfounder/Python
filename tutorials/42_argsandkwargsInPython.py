# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

# function_name_print("Manisha", "Kaushal", "Harry", "Mahi")


def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(key, value)


listOfName = ["Harry", "Manisha", "Kaushal", "Kunal"]
kw = {"Name": "Manisha", "Hobby": "Programming", "Class": "Nursery"}
normal = "I am a normal argument and The Students names are: "
funargs(normal, *listOfName, **kw)
