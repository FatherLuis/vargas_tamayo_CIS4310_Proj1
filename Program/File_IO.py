import os
from tkinter import filedialog
import re

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

        try:
            # Opens file from filepath # Read Only
            file = open('' + self.file + '', 'r')

            # CREATES A LIST STRING THAT WILL HOLD EACH LINE FROM THE TEXT FILE
            lineString = []

            # ITERATES THROUGH EACH LINE OF THE FILE AND APPENDS TO THE LIST
            for line in file:
                lineString.append(line)



        except:

            # IF ANY ERROR, FILE IS CLOSED AND USER WILL BE NOTIFIED THAT THE FILE WAS NOT USED
            self.fileName = 'No File Selected'
        else:
            # FILE IS CLOSED
            file.close()