# class for documents
class X:
    def __init__(self, input_data):
        # copy input DATA
        self.data = input_data
        # set group to none
        self.group = 0
        # count how many words it has
        for k in range(len(input_data)):
            self.mean = self.mean + input_data[k].number
        # distances to help assignment to a group
        self.distance = 0
        self.new_distance = 0

    def distance(self, centr):
        self.new_distance = 0
        # count distance from centroid
        for i in range(len(self.data)):
            for j in range(len(centr.centroid)):
                if centr.centroid.data[j].name == self.data[i].name:
                    self.new_distance += abs(self.data[i].number - self.centroid.data[j].number) * (1 / self.mean)
        # if new distance is shorter than previous (or it is first assignment) assign this doc to this group
        if self.distance == 0 or self.new_distance < self.distance: #  uwaga! a co jesli to jest liczba bez przecinkow?!
            self.set_group(centr.number)

    # set group
    def set_group(self, g):
        self.group = g

    def __repr__(self):
        return "{}".format(self.data)

