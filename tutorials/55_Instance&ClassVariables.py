class Employee:
    no_of_leaves = 8


harry = Employee()
harry.name = "Harry"
harry.salary = 454
harry.role = "Instructor"
manisha = Employee()
manisha.name = "Manisha"
manisha.salary = 4534
manisha.role = "Programmer"

# print(harry.name)
print(harry.no_of_leaves)
print(manisha.no_of_leaves)
print(Employee.no_of_leaves)

Employee.no_of_leaves = 10

print(harry.no_of_leaves)
print(manisha.no_of_leaves)
print(Employee.no_of_leaves)

harry.no_of_leaves = 9

print(harry.no_of_leaves)
print(manisha.no_of_leaves)
print(Employee.no_of_leaves)

print(harry.__dict__)
print(Employee.__dict__)
