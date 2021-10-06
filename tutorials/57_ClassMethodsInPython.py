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


harry = Employee("Harry", 2312, "Instructor")
manisha = Employee("Manisha", 122300002342342, "Student")

# Employee.no_of_leaves = 89\
print(manisha.no_of_leaves)
harry.change_leaves(12)
print(manisha.no_of_leaves)
print(harry.no_of_leaves)
