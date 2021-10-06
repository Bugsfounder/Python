# CREATE A CLASS PROGRAMMER FOR STORING INFORMATION OF FEW PROGRAMMERS WORKING AT MICROSOFT
from typing import Type


class Programmer:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getLanguage(self):
        return self.language

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def setLanguage(self, language):
        self.language = language

    def getDetails(self):
        return f"The Name of Programmer is {self.name}. Language of Programmer is {self.salary} and {self.language}"


manisha = Programmer("Manisha", 123213213, "Python")
print(manisha.getDetails())
