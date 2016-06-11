import classifier
import sys
import datascraper 
import pickle
from trainer import LanguageClassifier

def decide():
    nn = pickle.load(open('nn.pkl', 'r'))
    input = sys.argv[1]
    input = open(input, 'r').read()
    
    res = (datascraper.scrape([input], "?"))[0]
    X_input = res[0]
    answer = nn.decide(X_input)
    if answer == 2:
        print "The code was Python!"
    elif answer == -2:
        print "The code was SML"
    elif answer == 1:
        print "The code was Java"
    else:
        print "The code was C"

def main():
    decide()

if __name__=='__main__':
    main()
