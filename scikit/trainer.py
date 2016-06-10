import datascraper
import pickle
import numpy
import random
from sknn.mlp import Classifier, Layer

def createArrays():
    datalist = datascraper.finalLists()
    cList = datalist[0]
    pyList = datalist[1]
    smlList = datalist[2]
    javaList = datalist[3]
    
    outputList = cList + pyList + smlList + javaList
    random.shuffle(outputList)
    
    X_train = numpy.ndarray(shape=(len(outputList), 16))
    Y_train = numpy.ndarray(shape=(len(outputList), 4))
    for i in range(0, len(outputList)):
        data = outputList[i][0]
        answer = outputList[i][1]
        if answer == ".c":
            Y_train[i] = numpy.array([1,0,0,0])
        elif answer == ".py":
            Y_train[i] = numpy.array([0,1,0,0])
        elif answer == ".sml":
            Y_train[i] = numpy.array([0,0,1,0])
        elif answer == ".java":
            Y_train[i] = numpy.array([0,0,0,1])
        X_train[i] = numpy.array(data)
    return (X_train, Y_train, len(outputList))
    
def train():
    res = createArrays()
    X_train = res[0]
    Y_train = res[1]
    samples = res[2]
    nn = Classifier(
            layers=[
                Layer("Sigmoid", units=150),
                Layer("Softmax")
                ],
            learning_rate=0.001,
            n_iter=samples
            )
    nn.fit(X_train, Y_train)
    pickle.dump(nn, open('nn.pkl', 'wb'))

def main():
    train()

if __name__=='__main__':
    main()

