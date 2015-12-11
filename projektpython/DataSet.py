#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
from Vector import Vector

class Dataset():

    def __init__(self, instanceList):
        # print "type of instanceList= " , type(instanceList), " and first attr in list= " ,type(instanceList[0])
        # assert (isinstance(instanceList[0], Vector)), "Data needs list of Instances !"
        self.instList = instanceList

    def getSize(self):
        return self.instList.__len__()

    def getListOfVectors(self):
        return self.instList

    def printData(self):
        print self.instList