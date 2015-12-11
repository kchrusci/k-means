#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
import os

class ListElement():
	def __init__(self, word, numOfOccurences, title):
		self.word = word
		self.numOfOccurences = numOfOccurences
		self.title = title
	def printEl(self):
		print(self.word, self.numOfOccurences, self.title)
	
	def getWord(self):
		return self.word

	def getnumOfOccurences(self):
		return self.numOfOccurences

	def getTitle(self):
		return self.title

def getData(textTitle):
	index=0
	myfile=open(textTitle, 'r')
	text = myfile.read()
	el=text.split()
	
	wordlist = [word for word in el if len(word)>3 and word!='that' and word!='this' and word!='with' and word!='which' and word!='some']
	return wordlist	



def getKey(custom):
    return custom.numOfOccurences


def calculateFreq(wordList, textTitle, length):
	uniqueWords = list(set(wordList))#get unigue words from text
	Finallist = list()
	Finallist = [0 for x in range (len(uniqueWords))]
	for i in range(len(uniqueWords)):
		Finallist[i] = ListElement(uniqueWords[i], 0, textTitle)# list of ListElements objects
	
	for uword in wordList:
		for element in Finallist:
			if element.word==uword:
				element.numOfOccurences+=1
	Finallist = sorted(Finallist, key=getKey, reverse=True) #sort by numOfOccurences in falling order
	Finallist = Finallist[:length]
	#for i in range(len(Finallist)):
	#	print(Finallist[i].word, Finallist[i].numOfOccurences, Finallist[i].title)
	return Finallist


def getAllFiles(catalog):
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

#calculateFreq(getData(f), f, 20) #- returns a list with ListElement objects: with word, numOfOccurences & title , and the length = 20


for f in getAllFiles('/home/patrycja/Desktop/python/text_files/tekst_files'):
	print('\n')
	for i in range(len(calculateFreq(getData(f), f, 20))):
		ListElement.printEl(calculateFreq(getData(f), f, 20)[i])





