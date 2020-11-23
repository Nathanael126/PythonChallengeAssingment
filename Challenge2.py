import math


class Circle:
    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = str(color)

    def getArea(self):
        return float(math.pi*(self.radius*self.radius))


class Cylinder(Circle):
    def __init__(self, height, radius, color):
        Circle.__init__(self, radius, color)
        self.height = float(height)

    def getVolume(self):
        return self.height*self.getArea()