# CREATE A CLASS PETS FROM A CLASS ANIMALS AND FURTHER CREATE CLASS DOG FROM PETS ADD A METHOD BARK TO CLASS DOG

class Animals:
    leg = 4
    eye = 2


class Pets(Animals):
    cat = 2
    dog = 3


class Dog(Pets):
    def bark(self):
        print("Bow.... Bow....")


dog = Dog()
dog.bark()
