# PYTHON PRACTICE PROBLEM 2 (EASY, 10 POINTS)
# DIVIDE THE APPLES
# HARRY HAS n apples. HARRY HAS SOME STUDENTS AMONG WHOM, HE WANT TO
# DISTRIBUTE APPLES. THESE N NUMBER OF APPLES ARE PROVIDED TO HARRY BY HIS
# FRIENDS AND HE CAN REQUEST FEW MORE OR FEW LESS APPLES.

# YOU NEED TO PRINT WHETHER A NUMBER IN RANGE MIN TO MAX IS A DIVISOR OF N OR NOT.

# INPUT:
# TAKE INPUT n, MIN AND MAX FROM THE USER

# OUTPUT:
# Print whether the numbers between mn and mx are divisors of “n” or not.
# If mn=mx, show that this is not a range, and mn is equal to mx. Show the
# result for that number.

# EXAMPLE:

# IF N IS 20 AND MIN=2 AND MAX=5

# OP:
# 2 IS A DIVISOR OF 20
# 3 IS NOT A DIVISOR OF 20
# ...
# 5 IS A DIVISOR OF 20


try:
    n = int(input("Enter Number of apples: "))
    mn = int(input("Enter minimun Number of apples: "))
    mx = int(input("Enter maximum number of apples: "))
    for i in range(mn, mx + 1):
        if mn == mx and n % mn == 0:
            print(f"{mn} is a divisor of {n}")
        elif mn == mx and n % mn != 0:
            print(f"{mn} is not a divisor of {n}")
        elif n % i == 0:
            print(f'{i} is a divisor of {n}')
        elif n % i != 0:
            print(f"{i} is not a divisor of {n}")
except Exception as e:
    print("Only Numbers are Allowed")
