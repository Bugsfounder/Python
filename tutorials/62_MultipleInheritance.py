class Employee:
    no_of_leaves = 10

    var = 8

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


class Player:
    no_of_games = 4

    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        print(f"The Name is {self.name} and The Game is {self.game}")


# class CoolProgrammer(Employee, Player):
class CoolProgrammer(Player, Employee):
    language = "c++"

    # var = 10

    def printLanguage(self):
        print(self.language)


harry = Employee("Harry", 12434243243232432, "Instructor")
manisha = Employee("Manisha", 122300002342342, "Student")

shubham = Player("Shubham", "Hockey")
# shubham.printDetails()
karan = CoolProgrammer("Karan", "CoolProgrammer")
# karan.printDetails()
# karan.printLanguage()
print(karan.var)
