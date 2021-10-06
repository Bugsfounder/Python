class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        print(f"Name is {self.name}. Salary is {self.salary} and Role is {self.role}")


# harry = Employee()
# manisha = Employee()

# harry.name = "Harry"
# harry.salary = 454
# harry.role = "Instructor"

# manisha.name = "Manisha"
# manisha.salary = 4534
# manisha.role = "Programmer"

# harry.printDetails()


# USING CONSTRUCTOR
harry = Employee("Harry", 2312, "Instructor")
harry.printDetails()
