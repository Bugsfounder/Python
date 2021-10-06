class Employee:
    no_of_leaves = 10

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


harry = Employee("Harry", 2312, "Instructor")
manisha = Employee("Manisha", 122300002342342, "Student")
karan = Employee.from_dash("Karan-200-Student")
# karan.printGood("Manisha")
Employee.printGood("Manisha")
