import os
from histogram import Histogram


def group_numbers(path):
    categories = []
    for element in os.listdir(path):
        categories.append(element)
    return len(categories)


def get_histograms(path, bad_words):
    histograms = []
    names = []
    for element in os.listdir(path):
        temp_path = os.path.join(path, element)
        for directory in os.listdir(temp_path):
            full_path = os.path.join(temp_path, directory)
            # for document in directory create histogram
            hist = Histogram(full_path)
            # process file
            hist.process_file(bad_words)
            # full-fill words and numbers table
            hist.get_words()
            # sort histogram
            hist_sort = hist.sort_histogram()
            # append histograms table with histogram of current document
            histograms.append(hist_sort)
            names.append(hist.push_name())
            pair = [histograms, names]
    return pair

