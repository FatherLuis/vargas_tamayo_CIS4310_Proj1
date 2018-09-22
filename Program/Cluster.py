import math
import random


class Cluster:

    def __init__(self, points, numCluster):
        # an array of points
        self.points = points
        self.numCluster = numCluster
        self.means = []

        self.ClusterPoints = []

    def createRandMean(self):

        for i in range(self.numCluster):
            self.mean.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])

            self.ClusterPoints.append([])

    def distanceFunction(self, x2, y2, x1, y1):

        return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))

    def clusterPlacement(self):

        for i in range(len(self.points)):

            placement = 0
            minDistance = 0

            for j in range(self.numCluster):

                if (j == 0):
                    minDistance = self.distanceFunction(self.means[i][0], self.means[i][1], self.points[i].getx(), self.points[i].gety())

                currentDistance = self.distanceFunction(self.means[i][0], self.means[i][1], self.points[i].getx(), self.points[i].gety())

                if(minDistance > currentDistance):
                    minDistance = currentDistance
                    placement = j

            self.clusterPoint[placement].append(self.points[i])

    def calculateClusterMean(self):

        for i in range(self.numCluster):

            xmean = 0
            ymean = 0

            for j in range(len(self.ClusterPoint[i])):
                xmean += self.ClusterPoint[i][j].getx()
                ymean += self.ClusterPoint[i][j].gety()

            self.mean[i] = [xmean, ymean]


    def Clustering(self):

        self.createRandMean()
        self.clusterPlacement()
        self.calculateClusterMean()





