# class for documents
class X:
    def __init__(self, input_data):
        # copy input DATA
        self.data = input_data
        # set group to none
        self.group = 0
        # count how many words it has
	self.mean=0
        for k in range(len(input_data.number)):
            self.mean = self.mean + input_data.number[k]
        # distances to help assignment to a group
        self.distance = 0.0
        self.new_distance = 0.0

    def distances(self, centr):
        self.new_distance = 0.0
        # count distance from centroid
        for i in range(len(self.data.name)):
            for j in range(len(centr.centroid.data.name)):
                if centr.centroid.data.name[j] == self.data.name[i]:
                    self.new_distance = abs(self.data.number[i] - centr.centroid.data.number[j]) * (1.0 / self.mean)
        # if new distance is shorter than previous (or it is first assignment) assign this doc to this group
        if self.distance == 0.0 or self.new_distance < self.distance: 
            self.set_group(centr.number)
	    self.distance=self.new_distance
	
    # set group
    def set_group(self, g):
        self.group = g

    def __repr__(self):
        return "{}".format(self.data.name)

