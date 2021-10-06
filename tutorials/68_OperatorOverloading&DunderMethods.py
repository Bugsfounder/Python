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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and Role is {self.role}"

    def __mul__(self, other):
        return self.salary * other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Harry", 32, "Instructor")
emp2 = Employee("Manisha", 545, "Student")
# print(emp1 + emp2)
# print(emp1 / emp2)
print(emp1 * emp2)
print(emp1 - emp2)
print(emp1 > emp2)

# print(emp1)
print(repr(emp1))
print(str(emp1))
