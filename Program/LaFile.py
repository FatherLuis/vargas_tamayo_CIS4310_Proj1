

import csv

class State():

    def __init__(self, name):
        self.name
        self.container = []

    def addInfo(self,value):
        self.container.append(value)

    def setName(name):
        self.name = name
        
        









class File_IO():
    
    def __init(self):
        self.fileName = ""
        self.states = []

    def ReadFile():
        

        with open(self.file) as csv_file:

            csv_reader = csv.reader(csv_file, delimiter = ",")
            index = 0

            for row in csv_reader:

                self.states.append(new State(row[0]))
                self.states[index].addInfo(row[1])
                self.states[index].addInfo(row[2])
                self.states[index].addInfo(row[3])
                self.states[index].addInfo(row[4])

                index +=1
                
                




















                


        
