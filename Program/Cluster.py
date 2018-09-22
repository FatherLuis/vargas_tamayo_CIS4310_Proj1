import random


class Cluster:

    def __init__(self,points, numCluster):
        self.points = points
        self.numCluster = numCluster
        self.means =[]


    def createMean(self):

        for i in range(self.numCluster):
            self.mean.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])


    def Clustering(self):

        self.createMean()
