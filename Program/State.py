# Class name: File_IO
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Has the functionality to read a text file and create a Rulebook
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none


class State:

    def __init__(self, name):
        self.name = name
        self.container = []

    def addInfo(self, value):
        self.container.append(value)

    def setName(self, name):
        self.name = name

    def getContainer(self):
        return self.container

    def getName(self):
        return self.name
