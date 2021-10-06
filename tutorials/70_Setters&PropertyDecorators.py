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


harry = Employee("Harry", "CodeWithHarry")
manisha = Employee("Manisha", "Mahi")

print(harry.explain())

# print(harry.email())
print(harry.email)

harry.fname = "Haris"
# print(harry.email())
print(harry.email)

harry.email = "this@this.com"
print(harry.explain())

del harry.email

print(harry.email)
