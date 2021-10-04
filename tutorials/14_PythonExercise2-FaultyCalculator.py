# EXERCISE 2 :- FAULTY CALCULATOR
# DESIGN A CALCULATO WHICH WILL CORRECTLY SOLVE ALL THE PROBLEMS EXCEPT TEH FOLLOWING ONES:-
# 45 * 3 = 555,
# 56 + 9 = 77,
# 56 / 6 = 4
# YOUR PROGRAM SHOULD TAKE OPERATOR AND THE TWO NUMEBRS AS INPUT FORM THE USER AND THAN RETURN THE RESULT

# operator, num1, num2, result
print("These are the operatrs: +, -, *, /, %")
operator = input("Enter Operator do you want to use: ")
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

result = num1 + num2
if num1 == 45 and num2 == 3 and operator == '*':
    result = 555
elif num1 == 56 and num2 == 9 and operator == "+":
    result = 77
elif num1 == 56 and num2 == 6 and operator == "/":
    result = 4
elif operator == '+':
    result = result
elif operator == "-":
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '%':
    result = num1 % num2

print(str(num1), operator, str(num2), "=", result)
