import string


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