import string


<<<<<<< HEAD
class Histogram:

    def __init__(self, document):
        self.h = dict()
        self.fp = open(self.document)
        self.table = []
        self.document = document
        self.word_flag = 0
        self.doc_name = ""
        self.words = []
        self.numbers = []

    def process_file(self, bad_words):
        self.word_flag = 0
        for line in self.fp:
            self.process_line(line, bad_words)
        return self.h

    def process_line(self, line, bad_words):
        line = line.replace('-', ' ')
        for word in line.split():
            word_flag = 0
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            for bad_word in bad_words:
                if bad_word == word:
                    word_flag = 1
            if word_flag == 0:
                self.h[word] = self.h.get(word, 0) + 1

    @staticmethod
    def total_words(h):
        return sum(h.values())

    @staticmethod
    def different_words(h):
        return len(h)

    def get_words(self):
        for key, value in h.items():
            self.words.append(key)
            self.numbers.append(value)

    def most_common(self, h):
        for key, value in h.items():
            self.table.append((value, key))

        self.table.sort(reverse=True)
        return self.table
=======
def process_file(document):
    h = dict()
    fp = open(document)
    for line in fp:
        process_line(line, h)
    return h


def process_line(line, h):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        h[word] = h.get(word, 0) + 1


def total_words(h):
    return sum(h.values())


def different_words(h):
    return len(h)


def most_common(h):
    table = []
    for key, value in h.items():
        table.append((value, key))

    table.sort(reverse=True)
    return table


hist = process_file('input/Sensor.txt')
print 'Histogram:', hist
print 'Total number of words:', total_words(hist)
print 'Number of different words:', different_words(hist)
print 'Most common word', most_common(hist)
>>>>>>> 71ab0b4113c427c5e773fcbef6609f562a0776bf
