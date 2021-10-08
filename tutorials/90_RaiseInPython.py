# a = input("What is Your Name: ")
# b = input("How much do you earn: ")
# if int(b) == 0:
#     raise ZeroDivisionError("B is zero so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello {a}")

# LETS ASSUME HERE IS SOME CODE THAT TAKES 1 HOUR FOR EXECUTE


# Task :- write about two built in exceltion in hindi

# 1. FileExistsError --> agar aap ek aisa file ya folder banane ki kosis karenge jo already bani hui ho to ye error raise hota hai
# 2. NotADirectoryError --> agar aap kisi ase file ko access karne ki kosis karte ho jo maujood na ho to ye error raise hota hai like agar aap use karte ho os.listdir()...

c = input("Enter Your Name: ")
try:
    print(a)
except Exception as e:
    if c == "manisha":
        raise ValueError("Manisha is Blocked She is not allowed")

    print("Exception Handled")
