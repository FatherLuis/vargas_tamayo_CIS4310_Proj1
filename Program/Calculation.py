from Program.Normalization import Normalization
from Program.Point import Point


class Calculation:

    def __init__(self, data):
        self.data = data
        self.min = []
        self.max = []
        self.Mean = []
        self.points = []

    def MaxMinCalculation(self):

        for i in range(len(self.data)):

            state = self.data[i].getContainer()

            for k in range(len(state)):

                if (i < 1):
                    self.min.append(state[k])
                    self.max.append(state[k])
                else:

                    if (state[k] < self.min[k]):
                        self.min[k] = state[k]
                    elif (state[k] > self.max[k]):
                        self.max[k] = state[k]

    def MeanCalculation(self):

        size = len(self.data)

        for i in range(size):

            state = self.data[i].getContainer()

            for k in range(len(state)):

                if (i < 1):
                    self.Mean.append(state[k])
                else:
                    self.Mean[k] += state[k]

        for j in range(len(self.Mean)):
            self.Mean[j] = self.Mean[j]/size


    def NormalizeCalculation(self):


        size = len(self.data)

        for i in range(size):

            state = self.data[i].getContainer()

            for k in range(len(state)):
                norm = Normalization(self.max[k], self.min[k], 1, 0)
                self.data[i].setInfo(k, norm.Normalize(state[k]))

    def PointCalculation(self):

        size = len(self.data)
        for i in range(size):
            sum = 0

            state = self.data[i].getContainer()
            for k in range(len(state)):
                if(not(k == 3)):
                    sum += state[k]

            self.points.append(Point(self.data[i].getName(), float(state[2]), float(sum/3)))

    def getPoints(self):
        return self.points


    def MainCalculation(self):

        self.MaxMinCalculation()
        self.MeanCalculation()
        self.NormalizeCalculation()
        self.PointCalculation()












