import os
from histogram import Histogram

input_path = 'input'  # path to input directory will be defined in main function of skeleton module
bad_words = ['an', 'the', 'for', 'with', 'in', 'on', 'through', 'a', 'to', 'under', 'over', 'or', 'is', 'are',
             'did', 'does', 'have', 'has', 'could', 'would', 'as', 'and', 'next', 'between', 'his', 'our', 'ours',
             'still', 'not', 'may', 'some', 'so', 'where', 'when', 'that', 'of', 'were', 'also', 'this', 'their',
             'yours', 'they', 'its', 'who', 'also', 'both', 'than', 'he', 'she', 'I', 'am', 'we', 'been', 'was'
             'had', 'out', 'each', 'every', 'be', 'above', 'up', 'down', 'all', 'more', 'many']


def group_numbers(path):
    categories = []
    for element in os.listdir(path):
        categories.append(element)
    return len(categories)


def get_histograms(path, bad_words):
    histograms = []
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
    return histograms

print group_numbers(input_path)
print get_histograms(input_path, bad_words)
