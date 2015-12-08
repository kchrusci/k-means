import string


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
