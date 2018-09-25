
# Class name: Normalization
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Normalize a numeric number to a given range
# Date: September 23, 2018
# List of changes with dates: none
# Special Notes: none


class Normalization:

    # Method Name: __init__
    # Purpose: Constructor
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def __init__(self, dtHigh, dtLow, nmHigh, nmLow):

        self.dataHigh = dtHigh
        #print(self.dataHigh)
        self.dataLow = dtLow
        #print(self.dataLow)
        self.normHigh = nmHigh
        #print(self.normHigh)
        self.normLow = nmLow
        #print(self.normLow)
        self.dataRange = self.dataHigh - self.dataLow
        #print(self.dataRange)
        self.normalizeRange = self.normHigh - self.normLow
        #print(self.normalizeRange)

    # Method Name: Normalize
    # Purpose: return a normalized number
    # Parameter: self,
    # Method used: none
    # Return Value: numeric
    # Date:  September 23, 2018
    def Normalize(self,num):
        
        number = num - self.dataLow
        dcNum = number/self.dataRange
        #print(dcNum)
        dNormNum = self.normalizeRange * dcNum
        #print(dNormNum)
        finalNormNum = self.normLow + dNormNum
        #print(finalNormNum)

        return finalNormNum

    # Method Name: DeNormalize
    # Purpose: return a denormalized number
    # Parameter: self,
    # Method used: none
    # Return Value: numeric
    # Date:  September 23, 2018
    def DeNormalize(self,number):

        dNormNum = number - self.normLow
        dcNum = dNormNum / self.normalizeRange
        num = dcNum * self.dataRange
        orinNum = num + self.dataLow

        return orinNum

