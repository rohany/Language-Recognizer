import random
import math

class Classifier:
    
    def __init__(self, inputVectorSize):
        self.weights = [random.uniform(-1,1) 
                for x in range(0, inputVectorSize+1)]
    def decide(self, inputData):
        result = 0
        inputData.append(1)
        for i in range(0, len(self.weights)):
            result += inputData[i]*self.weights[i]
        if result >= 0:
            return 1
        else:
            return -1
    
    #requires dataset is a list, where each element is a tuple,
    #containing an input vector as the first element, and the
    #"answer" as the second element of the tuple, answer is a 1 or -1
    #lc is the learning constant
    def train(self, dataset, lc):
        for i in range(0, 100):
            for d in dataset:
                data = d[0]
                data.append(1) #adding the bias element
                answer = d[1]
                res = self.decide(data)
                error = answer - res
                for i in range(0, len(self.weights)):
                    self.weights[i] = self.weights[i] + error * data[i] * lc            
