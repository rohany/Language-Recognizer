import pickle
from sknn.mlp import Classifier, Layer
import sys
import datascraper
import numpy
import trainer

def decide():
    nn = pickle.load(open('nn.pkl', 'rb'))
    input = sys.argv[1]
    input = open(input, 'r').read()
    
    res = (datascraper.scrape([input], "?"))[0]
    X_input = numpy.array([res[0]])
    answer = nn.predict(X_input)
    return answer

def main():
    res = decide()
    res = res[0]
    print(res)
    if res[0]==1:
        print "The code was C!"
    elif res[1]==1:
        print "The code was Python!"
    elif res[2]==1:
        print "The code was Standard ML!"
    elif res[3]==1:
        print "The code was Java!"

if __name__=='__main__':
    main()
