# PYTHON PRACTICE PROBLEM 1 (EASY, 10 POINTS)
# YOUR AGE IN 2090

# TAKE AGE OR YEAR OF BIRTH AS AN INPUT FORM USER AND DETECT INPUT IS AGE OR YEAR OF BIRTH AND TELL THEN WHEN WILL THEY BECOME 100 YEARS OLD.(5 POINTS)

# DO NOT USE ANY TYPE OF MODULES LIKE DATETIME OR DATE UTILS.(-5 POINTS) THEY CAN THEN OPTIONALLY PROVIDE A YEAR AND YOUR PROGRAM MUST TELL THEIR AGE IN THAT PARTICULAR YEAR.(3 POINTS)

# YOU SHOULD HAVE HANDLE ALL SORTS OF ERRORS LIKE (2 POINTS):
# YOU ARE NOT YET BORN --> IF SOMEONE ENTER FUTURE YEAR AS BIRTH OF YEAR
# YOU SEEMS TO BE THE OLDEST PERSON ALIVE --> IF SOMEONE AGE IS CROSSING GREATER Than 100
# YOU CAN ALSO HANDLE ANY OTHER ERRORS IF POSSIBLE

def ageDetector():
    try:
        userInput = int(input("Enter Your age or Birth of Year: "))
        year = 2021
        age = userInput
        userYear = userInput
        if userInput > 1900 and userInput <= year:
            age = year - userInput
            print(f"You Become 100 years old in {userInput + 100}")
        elif userInput < 100 and userInput > 0:
            boy = year - userInput
            userYear = boy
            print(f"You Become 100 years old in {boy + 100}")
        elif userInput > year:
            print("YOU ARE NOT YET BORN")
        elif userInput > 100:
            print("YOU SEEMS TO BE THE OLDEST PERSON ALIVE")
        elif userInput < 1900:
            print("Year Must be Greater Than 1900")
        else:
            print("Invalid date or Year Please Enter a Valid date as normal person age")
    except Exception as error:
        print("Enter a Valid input only Numbers allowed")
    else:
        try:
            optional = int(input("Enter Year to know your age on that year else press 0 for quite: "))
            us = optional - year
            if optional > 1900 and optional > year:
                print(f"Your age in {optional} is {us + age}")
            elif optional < 100 and optional > 0:
                morey = optional - age
                print(f"You Becomes {optional} Years old in {year + morey}")
            elif optional < year:
                y = year - optional
                print(f"You Becomes {age - y} Years old in {optional}")
            elif optional == 0:
                exit()
            else:
                print(f"Enter a valid Year. Year must be Greater than {userYear}")
        except Exception as error:
            print("Enter a Valid input only Numbers allowed")
    finally:
        print("****Thanks For Using Our App****")


if __name__ == '__main__':
    print("*********Welcome to Your Age in 2090*********")
    ageDetector()
