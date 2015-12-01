# class for documents
class X:
    def __init__(self, input_data):
        # copy input DATA
        self.data = input_data
        # set group to none
        self.group = 0
        # count how many words it has
        for k in len(input_data):
            self.mean = self.mean + input_data[k].number
        # distances to help assignment to a group
        self.distance = 0
        self.new_distance = 0

    def distance(self, centr):
        self.new_distance = 0
        # count distance from centroid
        for i in len(self.data):
            for j in len(centr.centroid):
                if centr.centroid[j].name == self.data[i].name:
                    self.new_distance += abs(self.data[i].number - self.centroid[j].number) * (1 / self.mean)
        # if new distance is shorter than previous (or it is first assignment) assign this doc to this group
        if self.distance == 0 or self.new_distance < self.distance:
            self.set_group(centr.number)

    # set group
    def set_group(self, g):
        self.group = g

    def __repr__(self):
        return "{}".format(self.data)


# class for groups
class C:
    def __init__(self, centr, n):
        self.nc = []
        self.centroid = centr  # starting centroid copied from some DATA
        self.flag = 0  # flag for stating that shift condition is met
        self.number = n + 1  # number of the group
        self.all = 0  # how many docs are in this group
        self.name_flag = 0  # for comparing names in centroid and docs
        self.mean = 0  # number of words in centroid

    # get all DATA of this group and calculate new centroid
    def calc_new(self, hist):
        for i in len(hist):  # go through all DATA
            if hist[i].group == self.number:  # check if doc belongs to this group
                self.all += 1  # increment member counter
                for j in len(hist[i]):  # check all the words in histogram
                    self.name_flag = 0
                    for k in len(self.nc):  # check for words already in centroid
                        if self.nc[k].name == hist[i][j].name:  # if it is already here just increase the value
                            self.nc[k].number = self.nc[k].number + hist[i][j].number
                            self.name_flag = 1
                    if self.name_flag == 0:  # if it wasnt already in centroid add it
                        self.nc.append(hist[i])
        for k in len(self.nc):
            self.nc[k].number /= self.all
        # how many words are there??
        for k in len(self.nc):
            self.mean = self.mean + self.nc[k].number
        # what is the difference between old and new centroid?
        if len(self.nc) != len(self.centroid):
            self.flag = 0  # big enough if there is new word (or lacks some old word)
        else:
            for k in len(self.nc):
                for l in len(self.centroid):
                    if self.nc[k].name == self.centroid[l].name:
                        self.c_shift += abs(self.nc[k].number - self.centroid[l].number) * (1 / self.mean)

        self.centroid = self.nc

    # min_shift - minimal shift
    def set_flag(self, min_shift):
        if self.c_shift < min_shift:
            self.flag = 1
        else:
            self.flag = 0


# main function
# get all docs and make of them class X objects
DATA = []
for i in len(raw_DATA):
    DATA.append(X(i))
# picking first centroids
groups = []
for i in range(20):
    groups.append(C(DATA[i], i))
# start looping
flag = 0
minimum = 0.001
while flag < len(groups):
    flag = 0
    # calculate distance for all DATA
    for i in len(DATA):
        for j in len(groups):
            DATA[i].distance(j)
    for j in len(groups):
        groups[j].calc_new(DATA)
        groups[j].set_flag(minimum)
        if groups[j].flag == 1:
            flag += 1
