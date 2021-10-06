# Public, Private & Protected Access Specifiers
class Employee:
    no_of_leaves = 10
    var = 8
    _protectedVar = 3
    __privateVar = 15

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        print(f"Name is {self.name}. Salary is {self.salary} and Role is {self.role}")

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print(f"This is good {string}")


harry = Employee("Harry", 12, "Programmer")

print(harry._Employee__privateVar)
