# class for documents
# input_data needs to have fields .words = [ word0 , word1 , ... , wordn ]
# and .number = [ number of word 0, ... ]
import logging
_logger = logging.getLogger(__name__)


class Probe:
    def __init__(self, input_data):
        # copy input DATA
        self.data = input_data
        # set group to none
        self.group = 0
        # count how many words it has
        self.total = 0
        for k in range(len(input_data.number)):
            self.total = self.total + input_data.number[k]
        # distances to help assignment to a group
        self.distance = 0.0
        self.new_distance = 0.0
        self.doc_name = ""

    def distances(self, centr, diff_words_distance):
        self.new_distance = 0.0
        # count distance from centroid
        for i in range(len(self.data.words)):
            _logger.info("Processing...")
            flag = 0
            for j in range(len(centr.centroid.data.words)):
                if centr.centroid.data.words[j] == self.data.words[i]:
                    self.new_distance = abs(self.data.number[i] - centr.centroid.data.number[j]) * (1.0 / self.total)
                    flag = 1
            if flag == 0:
                self.new_distance += diff_words_distance

        # if new distance is shorter than previous (or it is first assignment) assign this doc to this group
        if self.distance == 0.0 or self.new_distance < self.distance: 
            self.set_group(centr.number)
            self.distance = self.new_distance

    # set group
    def set_group(self, g):
        self.group = g

    def get_doc_name(self, name):
        self.doc_name = name

    def __repr__(self):
        return "{}".format(self.data.words)
