# crating histogram from input document
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

    # processing document
    def process_file(self, bad_words):
        self.word_flag = 0
        for line in self.fp:
            self.process_line(line, bad_words)
        return self.h

    # processing document line by line
    def process_line(self, line, bad_words):
        # replacing '-' for whitespace
        line = line.replace('-', ' ')
        for word in line.split():
            word_flag = 0
            # stripping by punctuation ad whitespace
            word = word.strip(string.punctuation + string.whitespace)
            # get lower case
            word = word.lower()
            # remove all bad_words
            for bad_word in bad_words:
                if bad_word == word:
                    word_flag = 1
            if word_flag == 0:
                self.h[word] = self.h.get(word, 0) + 1

    # return number of words
    def total_words(self):
        return sum(self.h.values())

    # return number of different words
    def different_words(self):
        return len(self.h)

    # append words and numbers tables
    def get_words(self):
        for key, value in self.h.items():
            self.words.append(key)
            self.numbers.append(value)

    # get numbers table
    def get_numbers(self):
        return self.numbers

    # sort histogram by numbers of word occurring
    def sort_histogram(self):
        for key, value in self.h.items():
            self.table.append((value, key))

        self.table.sort(reverse=True)
        return self.table

    # return document name
    def push_name(self):
        return self.doc_name



