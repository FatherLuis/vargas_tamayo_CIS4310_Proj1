





class Point:

    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.clusternumber = 0

    def getCoordinate(self):
        return str(self.name) + ": (" + str(self.x) + ", " + str(self.y) + ")"

    def getName(self):
        return self.name

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setClusterNumber(self, value):
        self.clusternumber = value
