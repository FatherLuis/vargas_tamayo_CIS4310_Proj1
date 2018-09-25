# Class name: State
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Object Stores the name of a state and the list of values
# Date: September 23, 2018
# List of changes with dates: none
# Special Notes: none


class State:

    # Method Name: __init__
    # Purpose: Constructor
    # Parameter: self, String Name
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def __init__(self, name):
        self.name = name
        self.container = []

    # Method Name: addInfo
    # Purpose: append data to list
    # Parameter: self, String numberic
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def addInfo(self, value):
        self.container.append(value)

    # Method Name: setName
    # Purpose: add data to name
    # Parameter: self, String Name
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def setName(self, name):
        self.name = name

    # Method Name: getContainer
    # Purpose: return the list
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def getContainer(self):
        return self.container

    # Method Name: setInfo
    # Purpose: place numeric value to selected index in list
    # Parameter: self, integer index, float value
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def setInfo(self, index, value):
        self.container[index] = value

    # Method Name: getName
    # Purpose: return variable name
    # Parameter: self, String Name
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def getName(self):
        return self.name
