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
	self.c_shift

    # get all DATA of this group and calculate new centroid
    def calc_new(self, hist):  # hist = DATA ( list of X-class objects)
	# clear all the DATA in new centroid
        for i in range(len(self.nc.data.name)):
		del self.nc.data.name[0]  # delete 0-element and do so as long as list is not empty
	for i in range(len(hist)):  # go through all DATA
            if hist[i].group == self.number:  # check if it belongs to this group
                self.all += 1  # increment group member counter
                for j in range(len(hist[i].data.name)):  # check all the words in X'class histogram
                    self.name_flag = 0
                    for k in range(len(self.nc.data.name)):  # check for words already in centroid
                        if self.nc.data.name[k] == hist[i].data.name[j]:  # if it is already here just increase the value
                            self.nc.data.number[k] = self.nc.data.number[k] + hist[i].data.number[j]
                            self.name_flag = 1
                    if self.name_flag == 0:  # if it wasnt already in centroid add it
                        self.nc.data.name.append(hist[i].data.name[j])
			self.nc.data.number.append(hist[i].data.number[j])

	# na razie niech zostanie zakomentowane ale wydaje mi sie ze to jest blad, nie wiem czemu to mialo sluzyc
        # for k in len(self.nc):
        #    self.nc[k].number /= self.all

        # how many words are there??
	self.mean = 0
        for k in range(len(self.nc.data.number)):
            self.mean = self.mean + self.nc.data.number[k]
        #what is the difference between data in old and new centroid?
        if len(self.nc.data.name) != len(self.centroid.data.name):
            self.flag = 0  # big enough if there is new word (or lacks some old word)
        else:	#if the number of words is even calculate the difference
            for k in range(len(self.nc.data.name)):
                for l in range(len(self.centroid.data.name)):
                    if self.nc.data.name[k] == self.centroid.data.name[l]:
                        self.c_shift += abs(self.nc.data.number[k] - self.centroid.data.number[l]) * (1 / self.mean)

        self.centroid = self.nc

    # min_shift - minimal shift
    def set_flag(self, min_shift):
        if self.c_shift < min_shift:
            self.flag = 1
        else:
            self.flag = 0


