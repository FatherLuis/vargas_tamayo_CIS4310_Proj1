



class Calculation:

    def __init__(self, data):
        self.data = data
        self.min = []
        self.max = []

    def MeanCalculation(self):
        for i in range(len(self.data)):

            state = self.data[i].getContainer()

            for k in range(len(state)):

                if (i < 1):
                    min.append(state[k])
                    max.append(state[k])
                else:

                    if (state[k] < self.min[k]):
                        self.min[k] = state[k]
                    elif (state[k] > self.max[k]):
                        self.max[k] = state[k]

    def MainCalculation(self):

        MeanCalculation()
        print("")







