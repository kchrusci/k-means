# class for groups
import logging
_logger = logging.getLogger(__name__)


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
        self.nc.data.number = []
        # go through all DATA
        for i in range(len(hist)):
            _logger.info("Processing...")
            if hist[i].group == self.number:  # check if it belongs to this group
                self.all += 1  # increment group member counter
                for j in range(len(hist[i].data.words)):  # check all the words in X'class histogram
                    self.name_flag = 0
                    for k in range(len(self.nc.data.words)):  # check for words already in centroid
                        # if it is already here just increase the value
                        if self.nc.data.words[k] == hist[i].data.words[j]:
                            self.nc.data.number[k] = self.nc.data.number[k] + hist[i].data.number[j]
                            self.name_flag = 1
                    if self.name_flag == 0:  # if it wasn't already in centroid add it
                        self.nc.data.words.append(hist[i].data.words[j])
                        self.nc.data.number.append(hist[i].data.number[j])

        # divide all numbers by number of docs in this group
        for k in range(len(self.nc.data.number)):
            self.nc.data.number[k] /= (1.0 * self.all)

        # how many words are there??
        for k in range(len(self.nc.data.number)):
            self.total = self.total + self.nc.data.number[k]
        # what is the difference between data in old and new centroid?
        if len(self.nc.data.words) != len(self.centroid.data.words):
            self.flag = 0  # big enough if there is new word (or lacks some old word)

        else:   # if the number of words is even calculate the difference
            for k in range(len(self.nc.data.words)):
                for l in range(len(self.centroid.data.words)):
                    if self.nc.data.words[k] == self.centroid.data.words[l]:
                        self.c_shift += abs(self.nc.data.number[k] - self.centroid.data.number[l]) * (1000.0 /
                                                                                                      self.total)

        self.centroid = self.nc

    # min_shift - minimal shift
    def set_flag(self, min_shift):
        if self.c_shift < min_shift:
            self.flag = 1
        else:
            self.flag = 0

    def most_common_in_group(self):
        most_common_words = []
        most_common_numbers = []
        for i in xrange(0, len(self.centroid.data.words)):
            # Five most common words in groups
            if len(self.centroid.data.words) < 5:
                max_number = len(self.centroid.data.words)
            else:
                max_number = 5
            if len(most_common_words) < max_number:
                most_common_words.append(self.centroid.data.words[i])
                most_common_numbers.append(self.centroid.data.number[i])
            else:
                # get the number and the name of most common word used in this (already sorted) histogram of centroid
                number = self.centroid.data.number[i]
                j = 0
                # go through out temporary "centroids"
                while j < max_number:
                    # to check if this particular histogram is better suited than any temporary
                    temp_number = most_common_numbers[j]
                    if number > temp_number:
                        # shift the list for words
                        most_common_words[(j+1):len(most_common_words)] = most_common_words[j:(len(most_common_words)-1)]
                        # and add the new temp histogram on appropriate position
                        most_common_words[j] = self.centroid.data.words[i]

                        # shift the list for numbers
                        most_common_numbers[(j+1):len(most_common_numbers)] = \
                            most_common_numbers[j:(len(most_common_numbers)-1)]
                        # and add the new temp histogram on appropriate position
                        most_common_numbers[j] = self.centroid.data.number[i]
                        break  # it is placed on list so end loop and check the next histogram
                    else:
                        j += 1
        return most_common_words
