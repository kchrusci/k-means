# main function
# get all docs and make of them class X objects
DATA = []
for i in range(len(raw_DATA)):
    DATA.append(X(i))
# picking first centroids
groups = []

# find the most common words to set them as centroids

# here should be function to find the 9 most used words 
# and create X-class object of it with: the word as .name and .number should be equal to most uses in one file
# then make a list of it -> first_centroids = [ ... ]	

for i in range(9):
    groups.append(C(first_centroids[i], i))

# start looping
flag = 0
# set minimum centroid shift
minimum = 0.001
while flag < len(groups):
    flag = 0
    # calculate distance for all DATA
    for i in range(len(DATA)):
        for j in range(len(groups)):
            DATA[i].distances(j)
	DATA[i].distance=0.0	# zero the distance for next iteration (because centroids may be further away??)
    # calculate new centroids and set(or not) flag that shift is good enough
    for j in range(len(groups)):
        groups[j].calc_new(DATA)
        groups[j].set_flag(minimum)
        if groups[j].flag == 1:
            flag += 1
