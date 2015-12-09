from probe import Probe
from cluster import Cluster
from histogram import Histogram
import os

path = 'input'
histograms = []

for element in os.listdir(path):
    temp_path = os.path.join(path, element)
    for directory in os.listdir(temp_path):
        full_path = os.path.join(temp_path, directory)
        hist = Histogram(full_path).sort_histogram()
        histograms.append(hist)

# main function
# import from both class Probe and C needed
# get all docs and make of them class Probe objects
DATA = []
for i in histograms:
    DATA.append(Probe(i))
# picking first centroids
groups = []

# find the most common words to set them as centroids
first_centroids = [];

# here should be function to find the 9 most used words
# and create Probe-class object of it with: the word as .name and .number should be equal to most uses in one file
# then make a list of it -> first_centroids = [ ... ]

for i in range(9):
    groups.append(Cluster(first_centroids[i], i))

# start looping
flag = 0
# set minimum centroid shift
minimum = 0.001
while flag < len(groups):
    flag = 0
    # calculate distances from centroids for all DATA
    for i in range(len(DATA)):
        for j in groups:
            DATA[i].distances(j)
    DATA[i].distance = 0.0  # zero the distance for next iteration (because centroids may be further away??)

    # calculate new centroids and set(or not) flag that shift is good enough
    for j in groups:
        j.calc_new(DATA)
        j.set_flag(minimum)
        if j.flag == 1:
            flag += 1

