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


class Programmer(Employee):
    no_of_holidays = 56

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printProg(self):
        print(
            f"The Programmer's Name is {self.name}. Salary is {self.salary}. Role is {self.role}. The Languages Are {self.languages}")


# harry = Employee("Harry", 2312, "Instructor")
# manisha = Employee("Manisha", 122300002342342, "Student")


harry = Programmer("Harry", 2312, "Instructor", ["Python", "Java", "C", "C++", "JavaScript", "PHP"])
manisha = Programmer("Manisha", 122300002342342, "Student", ["Python", "Java", "C", "C++", "JavaScript"])

shubham = Programmer("Shubham", 212, "Programmer", ["Python", "Java", "C"])
print(shubham.salary)
print(shubham.name)
print(shubham.no_of_holidays)
print(shubham.no_of_leaves)
shubham.printProg()
