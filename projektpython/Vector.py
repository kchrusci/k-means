#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
class Vector(list):


    # def __init__(self, coordinates):
    #     assert ( isinstance(coordinates, list)),"Vector needs list coordinates of multidimensional vector!"
    #     super(Vector, self).__init__(coordinates)

    def __init__(self):
        super(Vector, self).__init__()

    def getSize(self):
        return self.__len__()

    def printData(self):
        print super.__dict__