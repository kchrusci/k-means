import string
import os.path


class Histogram:

    def __init__(self, document):
        self.h = dict()
        self.document = document
        self.fp = open(self.document)
        self.table = []
        self.word_flag = 0
        self.doc_name = os.path.split(document)
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

    def total_words(self):
        return sum(self.h.values())

    def different_words(self):
        return len(self.h)

    def get_words(self):
        for key, value in self.h.items():
            self.words.append(key)
            self.numbers.append(value)

    def get_numbers(self):
        return self.numbers

    def sort_histogram(self):
        for key, value in self.h.items():
            self.table.append((value, key))

        self.table.sort(reverse=True)
        return self.table

    def push_name(self):
        return self.doc_name



