class Rectangle(object):
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count +=1
    def __add__(self, other):
        obj = Rectangle(self.width+other.width, self.height+other.height)
        return obj

    def isSquare(a, b):
        return a == b
    def calcArea(self):
        return self.width * self.height
    def printCount(cls):
        print(cls.count)

