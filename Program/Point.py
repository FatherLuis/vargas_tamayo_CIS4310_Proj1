# Class name: Point
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Object stores the name of th state and the coordinates of the given point in a list
# Date: September 23, 2018
# List of changes with dates: none
# Special Notes: none


class Point:

    # Method Name: __init__
    # Purpose: Constructor
    # Parameter: self, name, x ,y
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    # Method Name: getCoordinate
    # Purpose: return the coordinates of a given state
    # Parameter: self,
    # Method used: none
    # Return Value: string
    # Date:  September 23, 2018
    def getCoordinate(self):
        return str(self.name) + ": (" + str(self.x) + ", " + str(self.y) + ")"

    # Method Name: getName
    # Purpose: return the variable
    # Parameter: self
    # Method used: none
    # Return Value: string
    # Date:  September 23, 2018
    def getName(self):
        return self.name

    # Method Name: getx
    # Purpose: return the variable x
    # Parameter: self,
    # Method used: none
    # Return Value: numeric
    # Date:  September 23, 2018
    def getx(self):
        return self.x

    # Method Name:gety
    # Purpose: return the variable y
    # Parameter: self,
    # Method used: none
    # Return Value: numeric
    # Date:  September 23, 2018
    def gety(self):
        return self.y

