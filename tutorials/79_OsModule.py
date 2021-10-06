import os

# print(dir(os))
# print(os.getcwd())
# os.chdir("c:/program Files")
# os.chdir("c://")
# print(os.getcwd())


# print(os.listdir())
# os.chdir("c:/Program Files")
# print(os.listdir())
# print(os.listdir("c:"))

# os.mkdir("this")
# os.mkdir("this/that") --> this is not working for this type of operation
# os.makedirs("this/that/manisha.txt")

# os.rename("Manisha.txt", "manishaChanged.txt")

# print(os.environ.get("Path"))

# print(os.path.join("c://", "/manisha.txt"))

# print(os.path.exists("c://Program Files"))
# print(os.path.exists("c://Manisha"))

print(os.path.isfile("manisha2.txt"))
print(os.path.isfile("manisha.txt"))

print(os.path.isdir(".idea"))
print(os.path.isdir("manisha"))
