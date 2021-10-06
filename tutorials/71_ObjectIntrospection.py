class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}@{lname}.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.lname == None or self.fname == None:
            return "Email Not Set"
        return f"{self.fname}@{self.lname}.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split(".")[0]
        self.fname = names.split("@")[0]
        self.lname = names.split("@")[1]

    @email.deleter
    def email(self):
        self.lname = None
        self.fname = None


manisha = Employee("Manisha", "Kumari")

# print(manisha.fname)
# print(manisha.lname)
# print(manisha.email)

# print(type(manisha))
print(type("This is string"))

# print(id(manisha))
# print(id("This is string"))
# print(id("This is string"))
# print(id("This that that"))

o = "This is string"
# print(dir(o))
# print(dir(manisha))


import inspect

print(inspect.getmembers(manisha))
