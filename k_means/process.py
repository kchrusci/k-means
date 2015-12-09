
class Process:
    def __init__(self, histogram):
        self.words = []
        self.numbers = []
        for value, key in histogram:
            self.words.append(key)
            self.numbers.append(value)
