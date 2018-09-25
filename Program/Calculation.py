from Program.Normalization import Normalization
from Program.Point import Point

# Class name:
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class:
# Date: September 23, 2018
# List of changes with dates: none
# Special Notes: none


class Calculation:

    # Method Name: __init__
    # Purpose: Constructor
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def __init__(self, data):
        #stores the States in a list
        self.data = data
        #stores the min of each category in a list
        self.min = []
        #stores the max of each category in a list
        self.max = []
        #stores the Points in a list
        self.points = []

    # Method Name: MaxMinCalculation
    # Purpose: Find the max and min from the information stored in the states for each index
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def MaxMinCalculation(self):

        #ITEREATE BY THE SIZE OF STATES FOUND IN THE LIST
        for i in range(len(self.data)):
            #GET THE INFORMATION FROM EACH STATE IN THE GIVEN LIST
            state = self.data[i].getContainer()

            #ITERATE BY THE SIZE OF THE LIST
            for k in range(len(state)):

                # IF THIS IS THE FIRST STATE, LET THEM BE THE MIN AND MAX
                if (i < 1):
                    self.min.append(state[k])
                    self.max.append(state[k])
                else:
                    # CHECK IF THE INFORMATION IN CURRENT STATE IS LES THAN WHAT IS IN SELF.MIN
                    if (state[k] < self.min[k]):
                        self.min[k] = state[k]
                    # CHECK IF THE INFORMATION IN CURRENT STATE IS GREATER THAN WHAT IS IN SELF.MAX
                    elif (state[k] > self.max[k]):
                        self.max[k] = state[k]

    # Method Name: NormalizeCalculation
    # Purpose: Normalize data store in each category
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def NormalizeCalculation(self):

        #Number of states in the list
        size = len(self.data)

        #NUMBER OF CATEGORIES IN EACH STATE
        for i in range(size):
            #GET THE LIST OF CATEGORIES FOUND IN EACH STATE
            state = self.data[i].getContainer()

            #ACCORDING TO THE SIZE OF THE LIST
            for k in range(len(state)):
                norm = Normalization(self.max[k], self.min[k], 1, 0)
                self.data[i].setInfo(k, norm.Normalize(state[k]))

    # Method Name: PointCalculation
    # Purpose: turn 3D to 2D coordinates
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def PointCalculation(self):

        #NUMBER OF STATES IN THE LIST
        size = len(self.data)
        #NUMBER OF CATEGORIES IN EACH STATE
        for i in range(size):
            #INITIATE THE SUM
            sum = 0

            #GET THE CATEGORY LIST
            state = self.data[i].getContainer()
            for k in range(len(state)):
                #IGNORE THE THIRD CATEGORY
                if(not(k == 3)):
                    sum += state[k]
            #AAPPEND POINTS TO THE VARIBALE
            self.points.append(Point(self.data[i].getName(), float(state[2]), float(sum/3)))

    # Method Name: getPoints
    # Purpose: return list of Points
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def getPoints(self):
        return self.points

    # Method Name: MainCalculation
    # Purpose: so all the required procedures
    # Parameter: self,
    # Method used: MaxMinCalculation, NormalizeCalculation, PointCalculation
    # Return Value: none
    # Date:  September 23, 2018
    def MainCalculation(self):

        self.MaxMinCalculation()
        self.NormalizeCalculation()
        self.PointCalculation()












