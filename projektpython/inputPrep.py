#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
import os
import math


class ListElement():
	def __init__(self, word, numOfOccurences):
		self.word = word
		self.numOfOccurences = numOfOccurences
	def printEl(self):
		print(self.word, self.numOfOccurences)
	
	def getWord(self):
		return self.word

	def getnumOfOccurences(self):
		return self.numOfOccurences


def getForbiddenWords(pathToForbiddenWords):#returns the list of unimportant words, for example 'the', 'with'
	if False == os.path.isfile(pathToForbiddenWords):
		return -1
	myfile=open(pathToForbiddenWords, 'r')#directory where the forbidden words are
	text = myfile.read()
	el=text.split()
	return el

			 

def getKey(custom):
	if False==isinstance(custom, ListElement):
		return -1
	return custom.numOfOccurences


def getData(textTitle, pathToForbiddenWords):#returns a list of words from one file  - title: textTitle
	if False == os.path.isfile(pathToForbiddenWords):
		return -1
	if False == os.path.isfile(textTitle):
		return -1
	myfile=open(textTitle, 'r')
	text = myfile.read()
	el=text.split()
	
	wordlist = [word for word in el if len(word)>3 and word not in getForbiddenWords(pathToForbiddenWords)]
	return wordlist	


def calculateTf(wordList, length):# arguments = list of all words from file,length of the resulting words array
	uniqueWords = list(set(wordList))#get unigue words from text
	Finallist = list()
	Finallist = [0 for x in range (len(uniqueWords))]
	for i in range(len(uniqueWords)):
		Finallist[i] = ListElement(uniqueWords[i], 0)## list of ListElements objects
	
	for uword in wordList:
		for element in Finallist:
			if element.word==uword:
				element.numOfOccurences+=1
	Finallist = sorted(Finallist, key=getKey, reverse=True) #sort by numOfOccurences in falling order
	Finallist = Finallist[:length]

	return Finallist


def calculateIdf(listOfFiles, Finallist, pathToForbiddenWords):

	if False == os.path.isfile(pathToForbiddenWords):
		return -1
	idfList = list()
	numOfFiles = len(listOfFiles)
	numOfFWhereAppeared = 1
	idfList = [0 for x in range (len(Finallist))]
	for i in range(len(Finallist)):
		idfList[i] = ListElement(Finallist[i].getWord(), 0)
	
	for i in range(len(Finallist)):
		for cfile in listOfFiles:
			if Finallist[i].getWord() in getData(cfile, pathToForbiddenWords):
				numOfFWhereAppeared+=1
		#print "numOfFWhereAppeared:", numOfFWhereAppeared
		idfList[i] = math.log(numOfFiles/numOfFWhereAppeared)

		numOfFWhereAppeared = 1

	return idfList


def calculateTfIdf(idfList, Finallist):
	resultList = list()
	resultList = [0 for x in range (len(Finallist))]
	tfList = list()
	tfList = [0 for x in range (len(Finallist))]
	for i in range(len(Finallist)):
		tfList[i] = Finallist[i].getnumOfOccurences()
		#print(tfList[i])
		
		resultList[i] = tfList[i]*idfList[i]

	return resultList
	

def getAllFiles(catalog):#returns a list of all files that will be analysed -> from specified directory and all subdirectories
	if False == os.path.isdir(catalog):
		return -1
	files=os.listdir(catalog)
	os.chdir(catalog)
	subdirectories = list()
	allfiles = list()
	#print(files)
	for f in files:
		if os.path.isdir(f):

			subdirectories.append(f)
		else: allfiles.append(f)
	
	for dir in subdirectories:
		files=os.listdir(dir)
		#print(files)
		for f in files:		
			filename = os.path.join(dir, f)
			allfiles.append(filename)
			
	return allfiles


def prepareInput(catalog, length, pathToForbiddenWords):
	if False == os.path.isdir(catalog):
		return -1
	if False == os.path.isfile(pathToForbiddenWords):
		return -1
	fileList = getAllFiles(catalog)
	inputList = list()

	for f in fileList:
		#print(f)
		
		inputList.append(calculateTfIdf(calculateIdf(getAllFiles(catalog), calculateTf(getData(f, pathToForbiddenWords), length), pathToForbiddenWords), calculateTf(getData(f, pathToForbiddenWords), length)))
	return inputList	


#inputlista =(prepareInput('/home/patrycja/Desktop/python/text_files/tekst_files/texts', 2, '/home/patrycja/Desktop/python/text_files/tekst_files/ForbiddenWords.txt'))# 1) path to directory with files to analyze - program takes files from this directory and subdirectories, 2) length of vector








