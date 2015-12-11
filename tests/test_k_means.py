#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=======================================
Clustering text documents using k-means
=======================================
    test_k_means.py for testing k_means project and projectpython from
    https://bitbucket.org/pythonAGH/pythonproject
"""

import unittest

from projektpython.KMeansFix import kMeans
from projektpython.inputPrep import prepareInput
from projektpython.DataSet import Dataset
import logging
import sys

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)


class TestKMeans(unittest.TestCase):
    path = '../input'
    text_file = '../projektpython/ForbiddenWords.txt'
    cluster_number = 3
    iter_number = 3

    def __init__(self, path, text_file, cluster_number, iter_number):
        self.data_path = path
        self.forbidden_words = text_file
        self.number_of_cluster = cluster_number
        self.number_of_iter = iter_number

    def test_k_means_fix(self):
        data = Dataset(prepareInput(self.data_path, 10, self.forbidden_words))
        # Input documents
        input_groups = data.getListOfVectors()
        k_means = kMeans(data, self.number_of_cluster, self.number_of_iter)
        # Output clastered documents
        output_groups = k_means.getListOfVectors()

        print("Input groups: ", input_groups)
        print ("Output groups: ", output_groups)


if __name__ == "__init__":
    unittest.init()
