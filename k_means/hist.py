# This file is just for tests purpose and will be deleted
import string
import os.path


def process_file(document):
    h = dict()
    fp = open(document)
    doc_name = os.path.split(document)
    for line in fp:
        process_line(line, h)
    return h


def process_line(line, h):
    bad_words = ['an', 'the', 'for', 'with', 'in', 'on', 'through', 'a', 'to', 'under', 'over', 'or', 'is', 'are',
                 'did', 'does', 'have', 'has', 'could', 'would', 'as', 'and', 'next', 'between', 'his', 'our', 'ours',
                 'still', 'not', 'may', 'some', 'so', 'where', 'when', 'that', 'of', 'were', 'also', 'this', 'their',
                 'yours', 'they', 'its', 'who', 'also', 'both', 'than', 'he', 'she', 'I', 'am', 'we', 'been', 'was'
                 'had', 'out', 'each', 'every', 'be', 'above', 'up', 'down', 'all', 'more', 'many']
    line = line.replace('-', ' ')
    for word in line.split():
        word_flag = 0
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        for bad_word in bad_words:
            if bad_word == word:
                word_flag = 1
        if word_flag == 0:
            h[word] = h.get(word, 0) + 1


def total_words(h):
    return sum(h.values())


def different_words(h):
    return len(h)


def get_words(h):
    words = []
    numbers = []
    for key, value in h.items():
        words.append(key)
        numbers.append(value)
    print words
    print numbers


def sort_histogram(h):
    table = []
    for key, value in h.items():
        table.append((value, key))

    table.sort(reverse=True)
    return table


def most_common(sort_histogram):
    words = []
    numbers = []
    for word, freq in sort_histogram[0:0]:
        words = [word]
        numbers = [freq]


def most_common_word(h):
    table = []
    for key, value in h.items():
            table.append((key, value))

    table.sort(reverse=True)
    x, y = table[0]
    words = [x]
    numbers = [y]
    print "Words:",  words
    print "Numbers:", numbers

#  Tests
path = 'input'
histograms = []

for element in os.listdir(path):
    temp_path = os.path.join(path, element)
    for directory in os.listdir(temp_path):
        full_path = os.path.join(temp_path, directory)
        hist = process_file(full_path)
        histograms.append(sort_histogram(hist))

print len(histograms)
for i in xrange(0, len(histograms)):
    print histograms[i]
