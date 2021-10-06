# WRITE A CLASS CALCULATOR CAPABLE OF FINDING SQUARE, CUBE AND SQUARE ROOT OF A NUMBER
import math


class Calculator:
    def __init__(self, number):
        self.number = number

    def getSquare(self):
        return self.number * self.number

    def getCube(self):
        return self.number * self.number * self.number

    def getSquareRoot(self):
        return math.sqrt(self.number)


cal = Calculator(5)

print(cal.getCube())
print(cal.getSquare())
print(cal.getSquareRoot())
