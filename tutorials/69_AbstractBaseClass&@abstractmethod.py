# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    side = 4

    def __init__(self, len, bre):
        self.length = len
        self.breadth = bre

    def printArea(self):
        return self.length + self.breadth


rec = Rectangle(12, 43)
print(rec.printArea())
