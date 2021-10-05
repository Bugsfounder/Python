# 1. WRITE A PYTHON PROGRAM TO DISPLAY A USER ENTER NAME FOLLOWED BY GOOD AFTERNOON USING INPUT() FUNCTION.

# name = input("Enter You Name: ")
# print(f"Good Afternoon, {name}")

# 2. WRITE A PROGRAM TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME ADD DATE
# LETTER = """DEAR <|NAME|>
#                     YOU ARE SELECTED!
#                     <|DATE|>"""


# name = input("Enter Your Name: ")
# date = input("Enter Interview Date: ")
#
# letter = f"Dear, {name}\n\tYou are Selected!\n\t{date}"
#
# print(letter)

# 3. WRITE A PROGRAM TO DETECT DOUBLE SPACES IN A STRING
str = "This  is String  and it is the world's  best String  Ever!"

newStr = str.replace("  ", " ")
print(newStr)
