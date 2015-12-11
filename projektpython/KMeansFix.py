#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
from Vector import Vector
from DataSet import Dataset
from random import randint
from inputPrep import prepareInput
from inputPrep import getAllFiles
import random


def assignToCluster(nrOfClusters, data, centroids):
    assert (isinstance(data, Dataset)), "There is no valid data"
    print "-->IN assignToCluster"

    # every Vector has its own cluster which belongs to
    assignment = []
    for i in range(0,data.getSize()):
        whichCluster = 0
        firstInstanceDistance = calculateDistance(data.getListOfVectors()[i], centroids.getListOfVectors()[0])
        for x in range(1, centroids.getListOfVectors().__len__()):
            dist = calculateDistance(data.getListOfVectors()[i], centroids.getListOfVectors()[x])
            if dist < firstInstanceDistance:
                firstInstanceDistance = dist
                whichCluster = x
        assignment.append(whichCluster)
    print "\tOUT assignment data to cluster centroid= ", assignment
    return assignment


def meanQuantizationError(nrOfClusters, data, assignment, centroids):
    assert (isinstance(data, Dataset)), "There is no valid data"
    print "-->IN meanQuantizationError"

    # mean Quantization Error
    D = [0.0 for x in range(0, nrOfClusters)]

    for i in range(0, data.getListOfVectors().__len__()):
        D[assignment[i]] += calculateDistance(data.getListOfVectors()[i], centroids.getListOfVectors()[assignment[i]])

    # divide by number of Vectors belonging to this cluster
    for q in range(0, nrOfClusters):
        if assignment.count(q) != 0:
            D[q] = D[q]/ assignment.count(q)
        else:
            D[q] = float("inf")
    print "\tOUT D (mean quantization error)// each field contains value for cluster= ", D, "\n"
    return D

def calculateNewCentroids(nrOfClusters, data, assignment, centroids):
    print "-->IN calculateNewCentroids"
    print "\tcentroids= ", centroids.getListOfVectors()

    # create DataSet object for centroids
    newCentroidsDataset = Dataset([Vector() for i in range(0, nrOfClusters)])

    # init with Zeros all Vectors
    for t in  range(0, newCentroidsDataset.getListOfVectors().__len__()):
        for q in range(0, data.getListOfVectors()[0].__len__()):
            newCentroidsDataset.getListOfVectors()[t].append(0)

    # arithmetic mean
    for i in range(0, data.getListOfVectors().__len__()):
        for x in range(0, data.getListOfVectors()[0].__len__()):
            newCentroidsDataset.getListOfVectors()[assignment[i]][x] += data.getListOfVectors()[i][x]

    for q in range(0, nrOfClusters):
        for x in range(0, data.getListOfVectors()[0].__len__()):
            if assignment.count(q) != 0:
                newCentroidsDataset.getListOfVectors()[q][x] = newCentroidsDataset.getListOfVectors()[q][x] / assignment.count(q)
            else:
                newCentroidsDataset.getListOfVectors()[q][x] = 0


    print "\t\nOUT list of new centroids= ", newCentroidsDataset.getListOfVectors(), "\n"
    return newCentroidsDataset


def calculateDistance(inst, centroid):
    # assert (isinstance(inst, Vector)), "There is no valid data: inst"
    # assert (isinstance(centroid, Vector)), "There is no valid data: centroid"
    #Mean squared error
    d = 0
    for i in range(0, inst.__len__()):
        d += ((inst[i] - centroid[i]) ** 2)
    return d

def findCentroids(nrOfClusters, data):
    # TODO write algorithm setting initial location of centroids
    print "-->IN findCentroids"
    centroidsList = Dataset([0  for i in range(0, nrOFCluster)])

    jump = (int((data.getSize()+1)/nrOfClusters) )
    for i in range(0,nrOfClusters):
        centroidsList.getListOfVectors()[i]= data.getListOfVectors()[jump * i]
    print "\tOUT Found centroids= ", centroidsList.getListOfVectors(), "\n"
    return centroidsList

def countDiff(oldD, newD):
    print "-->IN countDIff"
    if newD != 0:
        diff = float((oldD - newD) / newD)
    else:
        diff = float("inf")
    print "\tOUT Calculated diff= ", abs(diff), "\n"
    return abs(diff)


def kMeans(data, nrOFCluster, nrOfGivenIterations):

    centroids = findCentroids(nrOFCluster, data)
    listD = [[0 for i in range(0, nrOFCluster)], [0 for i in range(0, nrOFCluster)]]
    loopCounter = 0
    givenError = 0.5

    while loopCounter < nrOfGivenIterations:
        assignment = assignToCluster(nrOFCluster, data, centroids)

        # seeking for empty centroids
        empty = []
        for e in range(0, nrOFCluster):
            if assignment.count(e) == 0:
                empty.append(e)
        # print "empty ", empty, "\n\n"

        #collecting empty centroids
        emptyCentroid = Dataset([])
        emptyListD = [[], []]
        for q in range(0, empty.__len__()):
            emptyCentroid.getListOfVectors().append(centroids.getListOfVectors()[empty[q]])
            emptyListD[0].append(listD[0][empty[q]])
            emptyListD[1].append(listD[1][empty[q]])

        #calculation
        D = meanQuantizationError(nrOFCluster, data, assignment, centroids)
        centroids = calculateNewCentroids(nrOFCluster, data, assignment, centroids)
        numberOfExistingCluster = []

        if (loopCounter == 0):
            listD[0] = D
        else:
            if loopCounter == 1:
                listD[1] = D
            else:
                listD[0] = listD[1]
                listD[1] = D

            # check if all cluster have at least one Vector assigned
            # otherwise del from cluster, decrement nrOFCluster
            centroidsTmp = Dataset([])
            listDTmp= [[],[]]

            for z in range(0, centroids.getListOfVectors().__len__()):
                ctr = 0
                for q in range(0, centroids.getListOfVectors()[0].__len__()):
                    if centroids.getListOfVectors()[z][q] != 0:
                        ctr += 1
                if ctr == 0:
                    centroidsTmp.getListOfVectors().append(centroids.getListOfVectors()[z])
                    listDTmp[0].append(listD[0][z])
                    listDTmp[1].append(listD[1][z])
                else:
                    numberOfExistingCluster.append(z)

            #remove empty data from processing
            for q in range(0,centroidsTmp.getListOfVectors().__len__()):
                centroids.getListOfVectors().remove(centroidsTmp.getListOfVectors()[q])
                listD[0].remove(listDTmp[0][q])
                listD[1].remove(listDTmp[1][q])
                nrOFCluster -= 1

            #check if given error tha calculated
            QoS = 0
            for q in range(0, numberOfExistingCluster.__len__()):
                if countDiff(listD[0][q], listD[1][q]) < givenError:
                    QoS += 1


            if QoS == centroids.getListOfVectors().__len__():
                print "\n!!!!!!!!!!KONIEC!!!!!!!!!!"
                break

            #restore empty centroids
            centroids.getListOfVectors().extend(emptyCentroid.getListOfVectors())
            nrOFCluster += emptyCentroid.getListOfVectors().__len__()
            listD[1].extend(emptyListD[0])
            listD[0].extend(emptyListD[1])

            print "@@ centr= " , centroids.getListOfVectors()

        print "\n*******END OF LOOP " ,loopCounter, "\n"
        loopCounter += 1

    for i in range(len(assignment)):
        print assignment[i], getAllFiles('../input')[i]



nrOFCluster = 3
nrOfGivenIterations = 3

data = Dataset(prepareInput('../input', 10, '/home/kchrusci/Workspace/repo/k-means/projektpython/ForbiddenWords.txt'))
print "data = ", data.getListOfVectors()

kMeans(data,nrOFCluster,nrOfGivenIterations)
print(getAllFiles('/home/koper/PycharmProjects/First/Samples'))


