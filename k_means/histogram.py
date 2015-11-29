import string


class Histogram:
    def __init__(self, document):
        self.h = dict()
        self.fp = open(self.document)
        self.table = []
        self.document = document

    def process_file(self):
        for line in self.fp:
            self.process_line(line, self.h)
        return self.h

    @staticmethod
    def process_line(line, h):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            h[word] = h.get(word, 0) + 1

    @staticmethod
    def total_words(h):
        return sum(h.values())

    @staticmethod
    def different_words(h):
        return len(h)

    def most_common(self, h):
        for key, value in h.items():
            self.table.append((value, key))

        self.table.sort(reverse=True)
        return self.table
