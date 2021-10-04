# Try Except Exception Handling In Python
num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")
try:
    print("The sum of two numbers are: ", int(num1) + int(num2))
except Exception as error:
    print("Some error occurs", error)

print("This line is very important")
