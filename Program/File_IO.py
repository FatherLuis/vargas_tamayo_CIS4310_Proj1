import csv
import os
from tkinter import filedialog
from Program.State import State

# Class name: File_IO
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Has the functionality to read a text file and create a Rulebook
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none


class File_IO:

    # Method Name: __init__
    # Purpose: Class Constructor
    # Parameter: self, integer, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __init__(self):
        # class variable will hold the string name of a file
        self.fileName = ''
        self.states = []

    # Method Name: openFile()
    # Purpose: Class Constructor
    # Parameter: self, integer, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def openFile(self):

        # opens file dialog to get file path
        self.file = filedialog.askopenfilename()
        # get basic file names
        self.fileName = os.path.basename(self.file)

    # Method Name: readFile()
    # Purpose: Opens file and collects information
    # Parameter: self
    # Method used: createRuleBook()
    # Return Value: none
    # Date:  April 2, 2019

    def readFile(self):

        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            index = 0

            for row in csv_reader:

                stateObject = State(row[0])

                self.states.append(stateObject)
                self.states[index].addInfo(row[1])
                self.states[index].addInfo(row[2])
                self.states[index].addInfo(row[3])
                self.states[index].addInfo(row[4])

                print(self.states[index].getName())

                index += 1




