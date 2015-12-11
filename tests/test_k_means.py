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

    def test_001_k_means(self):
        self.data_path = '../input'
        self.forbidden_words = '../projektpython/ForbiddenWords.txt'
        self.number_of_cluster = 3
        self.number_of_iter = 3
        data = Dataset(prepareInput(self.data_path, 10, self.forbidden_words))
        k_means = kMeans(data, self.number_of_cluster, self.number_of_iter)


if __name__ == "__main__":
    unittest.main()
