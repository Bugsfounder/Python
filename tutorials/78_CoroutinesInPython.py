# def searcher():
#     import time
#     # SOME 4 SECOND TIME CONSUMING TASK
#     book = "This is a Book on Manisha The Genius Girl"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text in the book")
#         else:
#             print("Your text is not in the book")
#
#
# input("Press Any Key: ")
# search = searcher()
# next(search)
# search.send("Manisha")
# input("Press Any Key: ")
# search.send("Manisha The")
#
# input("Press Any Key: ")
# search.send("The")
#
# input("Press Any Key: ")
# search.send("This")
#
# input("Press Any Key: ")
# search.send("This is")
#
# input("Press Any Key: ")
# search.send("Book")
#
# input("Press Any Key: ")
# search.send("Nothing")
#
# search.close()


# QUICK QUIZ:-
import time


def finder():
    f = open("letter.txt")
    letter = f.read()
    time.sleep(2)

    while 1:
        let = (yield)
        if let in letter.lower():
            print(f"Yes {let} is in the letter")
        else:
            print(f"No {let} is not in the letter")


find = finder()
next(find)

userInput = input("Enter Something to Search in the letter: ")
find.send(userInput)

userInput = input("Enter Something to Search in the letter: ")
find.send(userInput)

userInput = input("Enter Something to Search in the letter: ")
find.send(userInput.lower())

find.close()
