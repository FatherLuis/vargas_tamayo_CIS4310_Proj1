

class Normalization:

    def __init__(self, dtHigh,dtLow,nmHigh,nmLow):

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
        
    def Normalize(self,num):
        
        number = num - self.dataLow
        dcNum = number/self.dataRange
        #print(dcNum)
        dNormNum = self.normalizeRange * dcNum
        #print(dNormNum)
        finalNormNum = self.normLow + dNormNum
        #print(finalNormNum)

        return finalNormNum
    
    def DeNormalize(self,number):

        dNormNum = number - self.normLow
        dcNum = dNormNum / self.normalizeRange
        num = dcNum * self.dataRange
        orinNum = num + self.dataLow

        return orinNum
        
        
#car = Normalization(4000,100,1,-1)
#print(car.Normalize(1000))

#print(car.DeNormalize(-0.54))
        
        
