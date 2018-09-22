





class Point:

    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getCoordinate(self):
        return str(self.name) + ": (" + str(self.x) + ", " + str(self.y) + ")"
