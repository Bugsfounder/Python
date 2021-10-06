# CREATE A LIBRARY CLASS
# METHODS TO DEFINE
# DISPLAY BOOK
# LEND BOOK - (WHO OWN THE BOOK OF NOT PRESENT IN THE LIBRARY)
# ADD BOOK
# RETURN BOOK
# HARRYLIBRARY = LIBRARY(LISTOFBOOKS, LIBRARY NAME)
# DICTIONARY: BOOK - NAME_OF_PERSON_WHO_BOOKED
# CREATE A MAIN FUNCTION ADN RUN AN INFINITE WHILE LOOP ASKING USERS FOR THEIR INPUT
def add(self, key, value):
    self[key] = value


class Library:
    # CONSTRUCTOR
    def __init__(self, libraryName, *listOfBooks):
        self.listOfBooks = list(listOfBooks)
        self.libraryName = libraryName
        self.lendedBook = {}

    # METHODS
    def displayBooks(self):
        print("These are the list of all books available in our library now:- ")
        for book in self.listOfBooks:
            print(book)

    def lendBook(self, bookName, userName):
        self.lendedBook[userName] = bookName
        self.listOfBooks.remove(bookName)

    def lendBooks(self, userName, *listOfBook):
        self.lendedBook[userName] = listOfBook
        for i in listOfBook:
            self.listOfBooks.remove(list(listOfBook[i]))

    def addBook(self, bookName):
        self.listOfBooks.append(bookName.capitalize())

    def addBooks(self, *bookName):
        for i in bookName:
            self.listOfBooks.append(list(bookName[i]))

    def returnBook(self, userName, bookName):
        if userName in self.lendedBook.keys():
            if self.lendedBook[userName] == bookName:
                self.lendedBook.pop(userName)
            else:
                return f"Check the Spelling Perfectly or user not valid"
        self.listOfBooks.append(bookName)


book = ["Book1", "Book2", "Book3", "Book4", "Book5"]
manishaLibrary = Library("ManishaLibrary", *book)
try:
    val = True
    while True:
        userName = input("Enter your name:- ")

        user_input = eval(input(f"Welcome {userName} to {manishaLibrary.libraryName} \n"
                                f"Enter (1) To display books we have\n"
                                f"Enter (2) To donate a book \n"
                                f"Enter (3) To Lend a book\n"
                                f"Enter (4) To return a book\n"
                                f"Enter (5) For exit"
                                f":- "))

        if user_input == 1:
            manishaLibrary.displayBooks()
        elif user_input == 2:
            bookName = input("Enter Book Name to Donate: ")
            manishaLibrary.addBook(bookName)

        elif user_input == 3:
            bookName = input("Enter Book Name: ")
            manishaLibrary.lendBook(bookName, userName)
            print("Book Lended")

        elif user_input == 4:
            bookName = input("Enter Book Name: ")
            manishaLibrary.returnBook(userName, bookName)
            print("Book Returned")

        elif user_input == 5:
            exitOrNot = input("Enter q for Exit: ")
            break
        else:
            print("Wrong input has been entered")

except Exception as error:
    print("Something went wrong Please Try Again")
