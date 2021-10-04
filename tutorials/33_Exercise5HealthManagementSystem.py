# Exercise 5: Health Management System
# 3 CLIENTS: HARRY, KAUSHAL, ARYAN
# TOTAL 6 FILES TO CREATE THAT STORE THE DIET LOG AND EXERCISE LOG FOR PER USER THREE USER 3 DIET LOG FILE AND THREE EXERCISE LOG FILE
# WRITE A FUNCTION THAT WHEN EXECUTED TAKES AS INPUT CLIENT NAME
# ONE MORE FUNCTION TO RETRIEVE EXCERCISE OR FOOD FOR ANY CLIENT

def getDate():
    import datetime
    return datetime.datetime.now()


print("If you are already an user than simply fill your details else enter you name to join")
print("You already a user or not (0 or 1): ")
alreadyUserOrNot = input("Enter 0 for no 1 for yes: ")
userName = input("Enter Your Name: ")
print("Press Diet or Exercise")
catUser = input("Choose one from above: ")
print("Press log for add one Retrieve for fetch available logs")
logOrRet = input("Choose one above : ")
date = getDate()


def logDetail(name, catUser, date, alreadyUserOrNot, logOrRet):
    try:
        if (alreadyUserOrNot == '1' or alreadyUserOrNot == 'yes') and (logOrRet.lower() == "retrieve"):
            if catUser.lower() == "diet":
                f = open(name + catUser + ".txt")
                print("Here is the all diets of", name)
                print(f.read())
                f.close()
            elif catUser.lower() == "exercise":
                f = open(name + catUser + ".txt")
                print("Here is the all exercise of", name)
                print(f.read())
                f.close()
            else:
                print("Check the spelling")
        elif (alreadyUserOrNot == '1' or alreadyUserOrNot.lower() == 'yes') and (logOrRet.lower() == "log"):
            if catUser.lower() == 'diet':
                newLog = input("Add new log of Diet: ")
                f = open(name + catUser + ".txt", "a+")
                d = str(date)
                f.write("[" + d + "] " + newLog + "\n")
                print("New log added to user ", name, "to", catUser)
                f.close()
            elif catUser.lower() == "exercise":
                newLog = input("Add new log of Exercise: ")
                f = open(name + catUser + ".txt", "a+")
                d = str(date)
                f.write("[" + d + "] " + newLog + "\n")
                print("New log added to user ", name, "to", catUser)
                f.close()
            else:
                print("Check the spelling")
        elif (alreadyUserOrNot == '0' or alreadyUserOrNot.lower() == 'no') and (logOrRet.lower() == "log"):
            if catUser.lower() == 'diet':
                newLog = input("Add First log of Diet: ")
                f = open(name + catUser + ".txt", "w+")
                d = str(date)
                f.write("[" + d + "] " + newLog + "\n")
                print("New log added to user ", name, "to", catUser)
                f.close()
            elif catUser.lower() == "exercise":
                newLog = input("Add First log of Exercise: ")
                f = open(name + catUser + ".txt", "w+")
                d = str(date)
                f.write("[" + d + "] " + newLog + "\n")
                print("New log added to user ", name, "to", catUser)
                f.close()
            else:
                print("Check the spelling")
        else:
            print("Check all Spelling perfectly")
    except Exception as error:
        print("Something went wrong Please Try again and fill all information carefully")


logDetail(userName, catUser, date, alreadyUserOrNot, logOrRet)
