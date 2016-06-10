import numpy
import os
import re

def openFiles(endType):
    buildList = []
    homeDir = "/home/rohany/neuralnetworks/languageDetector"
    datadir = ""
    if endType == ".c":
        datadir = homeDir + "/data/c/"
    elif endType == ".py":
        datadir = homeDir + "/data/python/"
    elif endType == ".sml":
        datadir = homeDir + "/data/sml/"
    elif endType == ".java":
        datadir = homeDir + "/data/java/"
    for i in os.listdir(datadir):
        f = open(datadir + i, 'r')
        buildList.append(f.read())
    return buildList

def scrape(files, endType):
    buildList = []
    for f in files:
        caseNum = len(re.findall("case", f))
        curlyNum = len(re.findall("{*}", f)) 
        mallocNum = len(re.findall("malloc", f))
        includeNum = len(re.findall("\#inlcude", f)) 
        publicNum = len(re.findall("public", f))
        classNum = len(re.findall("class", f))
        newNum = len(re.findall("new", f)) 
        colonNum = len(re.findall(":", f))
        semicolonNum = len(re.findall(";", f))
        arrowNum = len(re.findall("->", f))
        fnNum = len(re.findall("fn", f))
        funNum = len(re.findall("fun", f))
        letNum = len(re.findall("let", f))
        starNum = len(re.findall("\*", f))
        ampersandNum = len(re.findall("\&", f))
        importNum = len(re.findall("import", f))
        d = ([caseNum, curlyNum, mallocNum, includeNum, publicNum, 
                classNum, newNum, colonNum, semicolonNum, arrowNum, 
                    fnNum, funNum, letNum, starNum, ampersandNum, 
                    importNum], endType)
        buildList.append(d)
    return buildList

def finalLists():
    cFiles = openFiles(".c")
    pyFiles = openFiles(".py")
    smlFiles = openFiles(".sml")
    javaFiles = openFiles(".java")
    return (scrape(cFiles, ".c"), scrape(pyFiles, ".py"), 
            scrape(smlFiles, ".sml"), scrape(javaFiles, ".java"))


