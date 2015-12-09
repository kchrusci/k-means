#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file of k-means project.
To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
        kmeans = k_means.module:function

Then run `python setup.py install` which will install the command `kmeans`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.
"""
from probe import Probe
from cluster import Cluster
from process import  Process

import load
import first_centroids
import presentation
import argparse
import sys
import logging

from k_means import __version__

__author__ = "celinoslawa"
__copyright__ = "celinoslawa"
__license__ = "none"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="K-means demonstration")
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='k-means {ver}'.format(ver=__version__))
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    # path to input directory will be defined in main function of skeleton module
    input_path = 'input'
    # Unnecessary words that we would like to exclude from histogram
    bad_words = ['an', 'the', 'for', 'with', 'in', 'on', 'through', 'a', 'to', 'under', 'over', 'or', 'is', 'are',
                 'did', 'does', 'have', 'has', 'could', 'would', 'as', 'and', 'next', 'between', 'his', 'our', 'ours',
                 'still', 'not', 'may', 'some', 'so', 'where', 'when', 'that', 'of', 'were', 'also', 'this', 'their',
                 'yours', 'they', 'its', 'who', 'also', 'both', 'than', 'he', 'she', 'I', 'am', 'we', 'been', 'was'
                 'had', 'out', 'each', 'every', 'be', 'above', 'up', 'down', 'all', 'more', 'many', 'was']

    # main function
    # Create histograms from documents inside of categories
    histograms = load.get_histograms(input_path, bad_words)
    # Get number of categories
    number_of_groups = load.group_numbers(input_path)
    # Get all docs and make of them class Probe objects
    DATA = []
    for element in histograms:
        element = Process(element)
        DATA.append(Probe(element))

    # picking first centroids
    groups = []

    # find the most common words to set them as centroids
    first_cent = first_centroids.create_first_centroids(number_of_groups, histograms)

    # Create clusters
    for i in range(number_of_groups):
        groups.append(Cluster(first_cent[i], i))

    # start looping
    flag = 0
    # set minimum centroid shift
    minimum = 0.001
    while flag < len(groups):
        flag = 0
    # calculate distances from centroids for all DATA
        for i in range(len(DATA)):
            for j in groups:
                DATA[i].distances(j)
        DATA[i].distance = 0.0  # zero the distance for next iteration (because centroids may be further away??)

    # calculate new centroids and set(or not) flag that shift is good enough
        for j in groups:
            j.calc_new(DATA)
            j.set_flag(minimum)
            if j.flag == 1:
                flag += 1

    # Presentation of data
    presentation.get_presentation(groups, DATA)


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
