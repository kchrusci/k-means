
class Process:
    def __init__(self, histogram):
        self.words = []
        self.numbers = []
        self.distance = []
        self.distances = []
        self.data = []

        for value, key in histogram:
            self.words.append(key)
            self.numbers.append(value)
