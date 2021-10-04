# f = open("Manisha.txt") # IT TAKES DEFAULT READ MODE
# f = open("Manisha.txt", "r")  # READ MODE
# f = open("Manisha.txt", "rb")  # READ AS BINARY FORM
# f = open("Manisha.txt", "rt")  # READ AS TEXT FORM WHICH IS DEFAULT IF YOU DON'T GIVE STILL IT WORKING
# content = f.read()
# content = f.read(7)  # WE CAN PASS ARGUMENTS TO THE READ FUNC AS HOW MANY CHARACTERS DO YOU WANT TO READ
# content = f.read(743)  # WE CAN PASS ARGUMENTS TO THE READ FUNC AS HOW MANY CHARACTERS DO YOU WANT TO READ
# print(content)

# AS THIS FUNCTIONTION CALL AGAIN BUT STILL IT DOESN'T RETURN THE SAME VALUE AS FUNCTION ABOVE  IT READ NEXT SEVEN CHARACTER
# content = f.read(7)
# content = f.read(743)
# print(content)

# print(content)


# READ FILE USING ITERATIVE METHOD LINE BY LINE
f = open("Manisha.txt", "rt")
# content = f.read()

# READ FILE CHARACTER BY CHARACTER
# for line in content:
#     print(line)

# READ FILE LINE BY LINE
# for line in f:
#     print(line, end="")

# READLINE FUNCTION IN FILE I/O
# print(f.readline())
# print(f.readline())
# print(f.readline())

# READLINES FUNCTION IN FILE I/O
print(f.readlines())

f.close()
