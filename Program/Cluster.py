import math
import random


class Cluster:

    def __init__(self, points, numCluster):
        # an array of points
        self.points = points
        self.numCluster = numCluster
        self.means = []

        self.ClusterPoints = []

        self.information =" "

    def createRandMean(self):

        for i in range(self.numCluster):
            self.means.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])


    def distanceFunction(self, x2, y2, x1, y1):

        return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))

    def ClusterPlacement(self):

        self.ClusterPoints = []
        for i in range(self.numCluster):
            self.ClusterPoints.append([])

        for i in range(len(self.points)):

            placement = 0
            minDistance = 0

            for j in range(self.numCluster):

                if (j == 0):
                    minDistance = self.distanceFunction(self.means[j][0], self.means[j][1], self.points[i].getx(), self.points[i].gety())

                currentDistance = self.distanceFunction(self.means[j][0], self.means[j][1], self.points[i].getx(), self.points[i].gety())

                if(minDistance > currentDistance):
                    minDistance = currentDistance
                    placement = j

            #print(placement)
            self.ClusterPoints[placement].append(self.points[i])

    def CalculateClusterMean(self):

        for i in range(self.numCluster):
            #print("Cluster " + str(i))


            xmean = 0
            ymean = 0

            clusterSize = len(self.ClusterPoints[i])

            if(not(clusterSize == 0)):
                for j in range(clusterSize):
                    xmean += self.ClusterPoints[i][j].getx()
                    ymean += self.ClusterPoints[i][j].gety()

                self.means[i] = [xmean/clusterSize, ymean/clusterSize]
            #print(self.means[i])


    def Clustering(self):

        self.createRandMean()

        self.information = " "

        for i in range(50):
            self.ClusterPlacement()
            self.CalculateClusterMean()

        for i in range(self.numCluster):

            self.information += "\nCluster " + str(i) + ":\n\n"

            if(len(self.ClusterPoints[i]) ==0):
                self.information+= "  Empty Cluster \n"

            else:
                for k in range(len(self.ClusterPoints[i])):
                    self.information += "  " + self.ClusterPoints[i][k].getName() + "\n"


    def getInformation(self):
        return self.information







