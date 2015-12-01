# class for groups
class C:
    def __init__(self, centr, n):
	self.nc = centr #WYZEROWAC LUB STWORZYC PUSTY typu X(klasa od histogramu) 
        self.centroid = centr  # starting centroid copied from input DATA
        self.flag = 0  # flag for stating that centroid shift condition is met
        self.number = n + 1  # number of the group
        self.all = 0  # how many docs are in this group
        self.name_flag = 0  # for comparing names in centroid and docs
        self.mean = 0  # number of words in centroid

    # get all DATA of this group and calculate new centroid
    def calc_new(self, hist):  # hist = DATA ( list of X-class objects)
	# clear all the DATA in new centroid
        for i in range(len(nc.data)):
		del nc.data[0]	 #delete 0-element and do so as long as list is empty
	for i in range(len(hist)):  # go through all DATA
            if hist[i].group == self.number:  # check if it belongs to this group
                self.all += 1  # increment group member counter
                for j in range(len(hist[i].data)):  # check all the words in histogram
                    self.name_flag = 0
                    for k in range(len(self.nc.data)):  # check for words already in centroid
                        if self.nc[k].name == hist.data[i][j].name:  # if it is already here just increase the value
                            self.nc[k].number = self.nc.data[k].number + hist.data[i][j].number
                            self.name_flag = 1
                    if self.name_flag == 0:  # if it wasnt already in centroid add it
                        self.nc.data.append(hist[i].data[j])

	# na razie niech zostanie zakomentowane ale wydaje mi sie ze to jest blad, nie wiem czemu to mialo sluzyc
        # for k in len(self.nc):
        #    self.nc[k].number /= self.all

        # how many words are there??
	self.mean = 0
        for k in range(len(self.nc)):
            self.mean = self.mean + self.nc[k].number
        #what is the difference between data in old and new centroid?
        if len(self.nc.data) != len(self.centroid.data):
            self.flag = 0  # big enough if there is new word (or lacks some old word)
        else:	#if the number of words is even calculate the difference
            for k in range(len(self.nc.data)):
                for l in range(len(self.centroid.data)):
                    if self.nc.data[k].name == self.centroid.data[l].name:
                        self.c_shift += abs(self.nc[k].number - self.centroid[l].number) * (1 / self.mean)

        self.centroid = self.nc

    # min_shift - minimal shift
    def set_flag(self, min_shift):
        if self.c_shift < min_shift:
            self.flag = 1
        else:
            self.flag = 0


