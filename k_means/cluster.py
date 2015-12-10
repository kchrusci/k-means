# class for groups
# import from class X needed ??


class Cluster:
    def __init__(self, centr, n):
        self.nc = centr  # temporary centroid
        self.centroid = centr  # starting centroid copied from input DATA
        self.flag = 0  # flag for stating that centroid shift condition is met
        self.number = n + 1  # number of the group
        self.all = 0  # how many docs are in this group
        self.name_flag = 0  # for comparing names in centroid and docs
        self.total = 0  # number of words in centroid
        self.c_shift = 0.0

    # get all DATA of this group and calculate new centroid
    def calc_new(self, hist):  # hist => list of X-class objects
        # clear all the DATA in new centroid
        self.all = 0
        self.total = 0
        self.nc.data.words = []
        self.nc.data.numbers = []
        # go through all DATA
        for i in range(len(hist)):
            print "Working..."
            if hist[i].group == self.number:  # check if it belongs to this group
                self.all += 1  # increment group member counter
                for j in range(len(hist[i].data.words)):  # check all the words in X'class histogram
                    self.name_flag = 0
                    for k in range(len(self.nc.data.words)):  # check for words already in centroid
                        # if it is already here just increase the value
                        if self.nc.data.words[k] == hist[i].data.words[j]:
                            self.nc.data.numbers[k] = self.nc.data.numberss[k] + hist[i].data.numbers[j]
                            self.name_flag = 1
                    if self.name_flag == 0:  # if it wasn't already in centroid add it
                        self.nc.data.words.append(hist[i].data.words[j])
                        self.nc.data.numbers.append(hist[i].data.numbers[j])

        # divide all numbers by number of docs in this group
        for k in range(len(self.nc.data.numbers)):
            self.nc.data.numbers[k] /= (1.0 * self.all)

        # how many words are there??
        for k in range(len(self.nc.data.numbers)):
            self.total = self.total + self.nc.data.numbers[k]
        # what is the difference between data in old and new centroid?
        if len(self.nc.data.words) != len(self.centroid.data.words):
            self.flag = 0  # big enough if there is new word (or lacks some old word)

        else:   # if the number of words is even calculate the difference
            for k in range(len(self.nc.data.words)):
                for l in range(len(self.centroid.data.words)):
                    if self.nc.data.words[k] == self.centroid.data.words[l]:
                        self.c_shift += abs(self.nc.data.numbers[k] - self.centroid.data.numbers[l]) * (1.0 / self.total)

        self.centroid = self.nc

    # min_shift - minimal shift
    def set_flag(self, min_shift):
        if self.c_shift < min_shift:
            self.flag = 1
        else:
            self.flag = 0
