# We can take an example of a capsule in which the medicine is encapsulated. We have often used examples of bigger projects in which many programmers contribute according to their tasks. In the end, the whole project is done by joining the contribution of each participant. Well, this is what Encapsulation aims to achieve.

# Abstraction and Encapsulation are fundamental concepts of OOP. Encapsulation takes all the worry away from the user, providing him with just the product that he requires, irrespective of the way it is formed. Abstraction focuses on the working of the object instead of the how part, while Encapsulation is all about hiding the way or method of working and just providing the working model.

# Classes can be a perfect example of abstraction as each team member is given a separate class to work on, to develop a more significant project. A person working in a class only knows his job. While Encapsulation can be said to hide the code from normal users by making a front end through which the user can interact through the software without direct access to the code.


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")
