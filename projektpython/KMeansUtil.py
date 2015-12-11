#!/usr/bin/python
"""
Project from https://bitbucket.org/pythonAGH/pythonproject
"""
from Vector import Vector
from DataSet import Dataset
from random import randint


def assignToCluster(nrOfClusters, data, centroids):
    assert (isinstance(data, Dataset)), "There is no valid data"
    print "-->IN assignToCluster"
    # print "\tnrOfClusters= ", nrOfClusters, "\n\tdata= ", data.getListOfVectors(), "\n\tcentroids= ", centroids

    # every Vector has its own cluster which belongs to
    assignment = []
    for i in range(0,data.getSize()):
        whichCluster = 0
        firstInstanceDistance = calculateDistance(data.getListOfVectors()[i], centroids.getListOfVectors()[0])
        # print "firstDistance= " , firstInstanceDistance
        for x in range(1, centroids.getListOfVectors().__len__()):
            dist = calculateDistance(data.getListOfVectors()[i], centroids.getListOfVectors()[x])
            if dist < firstInstanceDistance:
                firstInstanceDistance = dist
                whichCluster = x
        assignment.append(whichCluster)
    print "\tOUT assignment data to cluster centroid= ", assignment, "\n"
    return assignment


def meanQuantizationError(nrOfClusters, data, assignment, centroids):
    assert (isinstance(data, Dataset)), "There is no valid data"
    print "-->IN meanQuantizationError"
    print "\tnrOfClusters= ", nrOfClusters, "\n\tdata= ", data.getListOfVectors(), "\n\tassignment=", assignment, "\n\tcentroids= ", centroids

    # mean Quantization Error
    D = [0.0 for x in range(0, nrOfClusters)]
    # print "D= ", D
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
    print "\tnrOfClusters= ", nrOfClusters, "\n\tdata= ", data.getListOfVectors(), "\n\tassignment=", assignment, "\n\tcentroids= ", centroids.getListOfVectors()

    # create DataSet object for centroids
    newCentroidsDataset = Dataset([Vector() for i in range(0, nrOfClusters)])
    # init with Zeros all Vectors
    for t in  range(0, newCentroidsDataset.getListOfVectors().__len__()):
        for q in range(0, data.getListOfVectors()[0].__len__()):
            newCentroidsDataset.getListOfVectors()[t].append(0)

    # arithmetic mean
    for i in range(0, data.getListOfVectors().__len__()):
        for x in range(0, data.getListOfVectors()[0].__len__()):
            # print "list of new centroids= ", listOfNewCentroids
            newCentroidsDataset.getListOfVectors()[assignment[i]][x] += data.getListOfVectors()[i][x]
            # print "list of new centroids after loop= ", listOfNewCentroids
    for q in range(0, nrOfClusters):
        for x in range(0, data.getListOfVectors()[0].__len__()):
            newCentroidsDataset.getListOfVectors()[q][x] = newCentroidsDataset.getListOfVectors()[q][x] / data.getListOfVectors()[0].__len__()


    print "\tOUT list of new centroids= ", newCentroidsDataset.getListOfVectors(), "\n"
    return  newCentroidsDataset


def calculateDistance(inst, centroid):
    assert (isinstance(inst, Vector)), "There is no valid data: inst"
    assert (isinstance(centroid, Vector)), "There is no valid data: centroid"
    #Mean squared error
    d = 0
    for i in range(0, inst.__len__()):
        d += ((inst[i] - centroid[i]) ** 2)
    return d

def findCentroids(nrOfClusters, data):
    # TODO write algo finding location of centroids
    print "-->IN findCentroids"
    print "\tnrOfClusters= ", nrOfClusters, "\n\tdata= ", data.getListOfVectors()
    centroidsList = Dataset([Vector() for i in range(0, nrOFCluster)])
    # print "\tcentroidsList= " , centroidsList.getListOfVectors()

    jump = (int((data.getSize()+1)/nrOfClusters) )
    # print "\tjump between indexes= ", jump
    for i in range(0,nrOfClusters):
        # print "\t\tposition=", i, " Vector= ",data.getListOfVectors()[jump * i]
        centroidsList.getListOfVectors()[i]= data.getListOfVectors()[jump * i]
    print "\tOUT Founded centroids= ", centroidsList.getListOfVectors(), "\n"
    return centroidsList

def countDiff(oldD, newD):
    print "-->IN countDIff"
    # print "\toldD= ", oldD, "\n\tnewD= ", newD
    if newD != 0:
        diff = float((oldD - newD) / newD)
    else:
        diff = float("inf")
    print "\tOUT Calculated diff= ", abs(diff), "\n"
    return abs(diff)

def reconcile(data, centroids, nrOFCluster, assignment, Dlist, whichCluster):
    print "-->IN reconcile"

    newData = Dataset([])
    newAssignment = []
    newCentroids = Dataset([])
    newDList= [[],[]]

    for x in range(0, data.getListOfVectors().__len__()):
        if assignment[x] == whichCluster:
            newData.getListOfVectors().append(data.getListOfVectors()[x])
            newAssignment.append(assignment[x])
            if newCentroids.getListOfVectors().__len__() == 0:

                newlist = [field for field in assignment]
                newlist.sort()
                counterTmp = [newlist[0]]
                for w in range(0, newlist.__len__()-1):
                    if newlist == whichCluster:
                        break
                    if newlist[w] != newlist[w+1]:
                        counterTmp.append(newlist[w+1])
                position = counterTmp.index(whichCluster)
                print newDList
                print Dlist
                print assignment[x]

                newCentroids.getListOfVectors().append(centroids.getListOfVectors()[position])
                newDList[0].append(Dlist[0][position])
                newDList[1].append(Dlist[1][position])
            print "\t ", x
    # newNrOFCluster = nrOFCluster - 1

    print "\nRECONCILIE:"
    print "## Data= ", newData.getListOfVectors()
    print "## Centroids= " , newCentroids.getListOfVectors()
    # print "## nrOFCluster" , newNrOFCluster
    print "## assignment=", newAssignment
    print "## Dlist=", newDList
    print "## Q= ", q
    print "which cluster=", whichCluster
    print "\n"

    return [newData, newCentroids, newAssignment, newDList]

def kMeans(data, nrOFCluster, nrOfGivenIterations):

    centroids = findCentroids(nrOFCluster, data)
    listD = [[0 for i in range(0, nrOFCluster)], [0 for i in range(0, nrOFCluster)]]
    loopCounter = 0
    givenError = 0.5

    while loopCounter < nrOfGivenIterations:
        assignment = assignToCluster(nrOFCluster, data, centroids)
        D = meanQuantizationError(nrOFCluster, data, assignment, centroids)
        centroids = calculateNewCentroids(nrOFCluster, data, assignment, centroids)
        numberOfExistingCluster = []

        if (loopCounter == 0):
            listD[0] = D
            print "@ListD in loop 0= " , listD
        else:
            if loopCounter == 1:
                listD[1] = D
            else:
                listD[0] = listD[1]
                listD[1] = D
            print "@nrOFCluster before loop=", nrOFCluster, "listD= ", listD



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
                    # print z
                    # print assignment[z]
            print "listDTmp=" , listDTmp
            print "centroidsTmp= ", centroidsTmp.getListOfVectors()
            print "~\n\n\nnumberOfExistingCluster= " ,numberOfExistingCluster


            for q in range(0,centroidsTmp.getListOfVectors().__len__()):
                centroids.getListOfVectors().remove(centroidsTmp.getListOfVectors()[q])
                listD[0].remove(listDTmp[0][q])
                listD[1].remove(listDTmp[1][q])
                nrOFCluster -= 1
            print "\n\nExtracted valid data "
            print "#Data= ", data.getListOfVectors()
            print "#centroids= ",  centroids.getListOfVectors()
            print "#nrOFCluster" , nrOFCluster
            print "#assignment=", assignment
            print "#listD= ", listD
            print "\n\n"


            newData = Dataset([])
            newAssignment = []
            newCentroids = Dataset([])
            newNrOfCluster = -1
            newDlist = [[],[]]
            datVecList = newData.getListOfVectors()
            centVecList = newCentroids.getListOfVectors()

            nrOFClustertemp = nrOFCluster
            for q in range(0, numberOfExistingCluster.__len__()):
                print "@@ ListD in loop= " , listD
                print "@@ Data= ", data.getListOfVectors()
                print "@@ centr= " , centroids.getListOfVectors()
                print "@@ nrOFCluster" , nrOFCluster
                print "@@ assignment=", assignment
                print "@@ Q in RECONCILIATION LOOP= ", q
                print "\n"

                if countDiff(listD[0][q], listD[1][q]) < givenError:
                    # print "nrOFCluster= " , nrOFCluster
                    datatemp, centroidstemp, assignmenttemp, listDtemp = reconcile(data,centroids,nrOFCluster, assignment, listD, numberOfExistingCluster[q])
                    datVecList += datatemp.getListOfVectors()
                    centVecList += centroidstemp.getListOfVectors()
                    nrOFClustertemp -= 1
                    newAssignment += assignmenttemp
                    newDlist[0] += listDtemp[0]
                    newDlist[1] += listDtemp[1]
                    print " #########x" , datVecList
                    print " #########x" , centVecList
                    print " #########x" , newNrOfCluster
                    print " #########x" , newAssignment
                    print " #########x" , newDlist


                # print "\nData after reconc:"
                # print "newData=", newData.getListOfVectors()
                # print "newCentroids", newCentroids.getListOfVectors()
                # print "nrOFCluster" , nrOFClustertemp
                # print "newAssignment" ,newAssignment
                # print "\n"

            for k in range(0, newData.getListOfVectors().__len__()):
                data.getListOfVectors().remove(newData.getListOfVectors()[k])
                assignment.remove(newAssignment[k])

            print "\nData after DELETION="
            print "newData=", data.getListOfVectors()
            print "assignment " , assignment

            for q in range(0,newCentroids.getListOfVectors().__len__()):
                centroids.getListOfVectors().remove(newCentroids.getListOfVectors()[q])
                listD[0].remove(newDlist[0][q])
                listD[1].remove(newDlist[1][q])
            print "newCentroids", centroids.getListOfVectors()
            print "Dlist ", listD

            # centroids = newCentroids
            # listD = newDlist
            nrOFCluster = nrOFClustertemp
            # data = newData
            # assignment = newAssignment

        print "*******Loop counter= " ,loopCounter
        loopCounter += 1

        if (data.getListOfVectors().__len__() == 0 ):
            break



#generato Instances
lengthOfVector = 2
countOfVectors = 7
nrOFCluster = 3
listOfInstances = []
nrOfGivenIterations = 3
for i in range(0,countOfVectors):
    #generator of random list
    instance = Vector()
    #instance.append(z for z in range(3 * (i + 1), 3 * (i + 5), 5))
    for q in range(1,lengthOfVector+1):
        instance.append(randint(1,20))
    # print "instance[", i , "] = ",  instance
    listOfInstances.append(instance)
# print "list of instances= " ,listOfInstances

#set DataSet containing list of Instances
data = Dataset(listOfInstances)
# print "data= ", data.getListOfVectors()

kMeans(data,nrOFCluster,nrOfGivenIterations)


''' Test of random Centroids
#random Centroids
centroids =  findCentroids(2, data)
print "initialized centroids", centroids
'''

''' Test of distance calculation
#find Distance
print "calculate distance between data[0] = ", data.getListOfVectors()[0], " and centroids[0] = ", centroids[0]
distance = calculateDistance(data.getListOfVectors()[0],centroids[0])
print "distance= " ,distance
'''