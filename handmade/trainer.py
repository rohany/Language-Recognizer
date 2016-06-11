import pickle
import datascraper
from classifier import Classifier
import random

def allArrays():
    datalist = datascraper.finalLists()
    cList = datalist[0]
    pyList = datalist[1]
    smlList = datalist[2]
    javaList = datalist[3]
    return (cList + pyList + smlList + javaList)

def JCarrays():
    datalist = datascraper.finalLists()
    cList = datalist[0]
    javaList = datalist[3]
    return (cList + javaList)
def PSarrays():
    datalist = datascraper.finalLists()
    pyList = datalist[1]
    smlList = datalist[2]
    return (pyList + smlList)


def trainJCfromSP():
    finalList = allArrays()
    def mapFunc(x):
        if x[1] == ".py" or x[1] == ".sml":
            listX = list(x)
            listX[1] = 1
            x = tuple(listX)
        else:
            listX = list(x)
            listX[1] = -1
            x = tuple(listX)
        return x
    dataList = []
    for x in finalList:
        dataList.append(mapFunc(x))
    random.shuffle(dataList)
    JCfromSP = Classifier(len(finalList[0][0]))
    JCfromSP.train(dataList, 0.05)
    return JCfromSP

def trainJfromC():
    finalList = JCarrays()
    def mapFunc(x): 
        if x[1] == ".java":
            listX = list(x)
            listX[1] = 1
            x = tuple(listX)
        else:
            listX = list(x)
            listX[1] = -1
            x = tuple(listX)
        return x
    dataList = []
    for x in finalList:
        dataList.append(mapFunc(x))
    random.shuffle(dataList)
    for x in finalList:
        x = mapFunc(x)
    JfromC = Classifier(len(finalList[0][0]))
    JfromC.train(dataList, 0.05)
    return JfromC
def trainSfromP():
    finalList = PSarrays()
    def mapFunc(x): 
        if x[1] == ".py":
            listX = list(x)
            listX[1] = 1
            x = tuple(listX)
        else:
            listX = list(x)
            listX[1] = -1
            x = tuple(listX)
        return x
    dataList = []
    for x in finalList:
        dataList.append(mapFunc(x))
    random.shuffle(dataList)
    SfromP = Classifier(len(finalList[0][0]))
    SfromP.train(dataList, 0.05)
    return SfromP

class LanguageClassifier:
    def __init__(self):
        self.JCfromSP = trainJCfromSP()
        self.JfromC = trainJfromC()
        self.SfromP = trainSfromP()

    def decide(self, inputVector):
        inputVector.append(1)
        firstFilter = self.JCfromSP.decide(inputVector)
        if firstFilter == 1:
            return self.SfromP.decide(inputVector)*2
        else:
            return self.JfromC.decide(inputVector)
    


    

def main():
    classifier = LanguageClassifier()
    pickle.dump(classifier, open('nn.pkl', 'w'))

if __name__=='__main__':
    main()

