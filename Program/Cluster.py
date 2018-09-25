import math
import random

# Class name: Cluster
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Allow for the allocation of information based on similaries
# Date: September 23, 2018
# List of changes with dates: none
# Special Notes: none
class Cluster:

    # Method Name: __init__
    # Purpose: Constructor
    # Parameter: self, point, numCluster
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def __init__(self, points, numCluster):
        # an array of points
        self.points = points
        # declares the number of clusteres needed to be created
        self.numCluster = numCluster
        # stores the coordinate means of each cluster [[],[],[],[]]
        self.means = []
        #STORES THE POINTS OBJECT IN A LIST BASED ON THEIR CLUSTERS [[C1POINT,C1POINT,...],[C2POINT,C2POINT,...],...]
        self.ClusterPoints = []
        #GETS THE STRING OF INFORMATION ABOUT EACH CLUSTER AND THE STATES INSIDE THEM
        self.information =" "

    # Method Name: CreateRanMean
    # Purpose: creates random coordinates in the form of a list [,]
    # Parameter: self,
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def createRandMean(self):

        #DEPENDING ON THE NUMBER OF CLUSTERS,
        for i in range(self.numCluster):
            #RANDOM FLOAT NUMBER IS CREATED BETWEEN O AND 1 INCLUSIVE
            self.means.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])

    # Method Name:distanceFunction
    # Purpose: calculate the distance between two points
    # Parameter: self, x2,y2,x1,y1
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def distanceFunction(self, x2, y2, x1, y1):
        #EUCLEDIAN DISTANCE FORMULA
        return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))

    # Method Name:ClusterPlacement
    # Purpose: place the Points in a cluster
    # Parameter: self
    # Method used: distanceFunction()
    # Return Value: none
    # Date:  September 23, 2018
    def ClusterPlacement(self):


        self.ClusterPoints = []
        #APPENDS EMPTY LIST INSIDE THE CLUSTERPOINTS LIST
        for i in range(self.numCluster):
            self.ClusterPoints.append([])

        # ITERATES THROUGH THE LIST OF POINTS
        for i in range(len(self.points)):

            #CLUSTER APPOINTED IN DEFAULT IF THEY DONT FIND A CLUSTER
            placement = 0
            #DISTANCE APPOINTED IN DEFAULT
            minDistance = 0

            #ITEREATES THROUGH ALL THE CLUSTER MEANS FOUND IN THE LIST
            for j in range(self.numCluster):
                #FOR THE FIRST ITERATION, THE MINIMUM MEAN IS THE DISTANCE BETWEEN THE CLUSTER O MEAN AND THE POINT
                if (j == 0):
                    minDistance = self.distanceFunction(self.means[j][0], self.means[j][1], self.points[i].getx(), self.points[i].gety())

                #ON THE FOLLOWING ITERATIONS, WE GET THE DISTANCE BETWEEN THE CLUSTER I MEAN AND THE POINT
                currentDistance = self.distanceFunction(self.means[j][0], self.means[j][1], self.points[i].getx(), self.points[i].gety())

                #IF THE MIN DISTANCE IS GREATER THAN THE CURRENTDISTANCE, IN OTHER WORKDS, THE DISTANCE BETWEEN THE POINT
                #AND CLUSTER I MEAN IS SMALLER, THEN THE CHANGE THE MINDISTANCE AND THE PLACEMENT
                if(minDistance > currentDistance):
                    minDistance = currentDistance
                    placement = j

            #POINT OBJECT IS SEND TO THE LIST OF LIST IN CLUSTERPOINTS ACCORDINGLY
            self.ClusterPoints[placement].append(self.points[i])

    # Method Name: CalculateClusterMean
    # Purpose: Calculate the mean of all the points in a given cluster
    # Parameter: self, numCluster
    # Method used: none
    # Return Value: none
    # Date:  September 23, 2018
    def CalculateClusterMean(self):

        #Iterate by the number of clusters found
        for i in range(self.numCluster):

            #WILL STORE THE MEAN OF THE X POINTS
            xmean = 0
            #WILL SORE THE MEAN OF THE Y POINTS
            ymean = 0

            #THE SIZE OF THE CLUSTER (NUMBER OF POINTS IN THE LIST)
            clusterSize = len(self.ClusterPoints[i])

            #IF THE CLUSTER IS NOT EMPTTY
            if(not(clusterSize == 0)):
                for j in range(clusterSize):
                    xmean += self.ClusterPoints[i][j].getx()
                    ymean += self.ClusterPoints[i][j].gety()

                self.means[i] = [xmean/clusterSize, ymean/clusterSize]


    # Method Name: Clustering
    # Purpose: main method that includes all fucntions in this class
    # Parameter: self,
    # Method used: clusterplacement, createRandMean, calculateClusterMean
    # Return Value: none
    # Date:  September 23, 2018
    def Clustering(self):

        #CREATE RANDOM POINTS FOR CLUSTERS
        self.createRandMean()

        self.information = " "

        #ITERATES 50 TIMES TO ENSURE ALL POINTS ARE IN THE CORRECT CLUSTER
        for i in range(50):
            self.ClusterPlacement()
            self.CalculateClusterMean()

        # THIS FOR LOOP WILL COLLECT ALL THE INFORMATION NEEDED TO BE RETREIVED
        # THAT INCLUDES THE CLUSTER NUMBER AND WHAT STATES ARE IN EACH CLUSTER.
        for i in range(self.numCluster):

            self.information += "\nCluster " + str(i) + ":\n\n"

            if(len(self.ClusterPoints[i]) ==0):
                self.information+= "  Empty Cluster \n"

            else:
                for k in range(len(self.ClusterPoints[i])):
                    self.information += "  " + self.ClusterPoints[i][k].getName() + "\n"

    # Method Name: getInformation
    # Purpose: return a string
    # Parameter: self,
    # Method used: none
    # Return Value: string
    # Date:  September 23, 2018
    def getInformation(self):
        return self.information







