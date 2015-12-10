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
from process import Process
import load
import first_centroids
import presentation
import argparse
import sys
import logging
from k_means import __version__

__author__ = ""
__copyright__ = ""
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
        version='k-means {ver}'.format(ver=__version__)
    )
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
    histograms = []
    names = []
    N = [histograms, names]
    _logger.info("Load documents from categories and create histograms")
    N = load.get_histograms(input_path, bad_words)
    histograms = N[0]
    names = N[1]
    # Get number of categories
    number_of_groups = load.group_numbers(input_path)
    # Get all docs and make of them class Probe objects
    DATA = []
    info = "Probe: " + str(len(histograms)) + " histograms"
    _logger.info(info)
    for element in histograms:
        element = Process(element)
        DATA.append(Probe(element))

    # picking first centroids
    groups = []
    # find the most common words to set them as centroids
    _logger.info("Choose first centroids")
    first_cent = first_centroids.create_first_centroids(number_of_groups, DATA)

    # create clusters
    # set minimum centroid shift
    minimum = 0.00001
    for i in range(number_of_groups):
        _logger.info("Create cluster")
        groups.append(Cluster(first_cent[i], i))
    # first iteration
    # calculate distances from centroids for all DATA
    for i in range(len(DATA)):
        for j in groups:
            _logger.info("Calculate distance")
            DATA[i].get_doc_name(names[i])
            DATA[i].distances(j, minimum)
        DATA[i].distance = 0.0  # zero the distance for next iteration (because centroids may be further away)

    # calculate new centroids and set(or not) flag that shift is good enough
    for j in groups:
        _logger.info("Calculate centroid")
        j.calc_new(DATA)

    # start looping
    flag = 0
    while flag < len(groups):
        _logger.info("Next iteration")
        flag = 0
    # calculate distances from centroids for all DATA
        for i in range(len(DATA)):
            for j in groups:
                _logger.info("Calculate distances")
                DATA[i].distances(j, minimum)
            DATA[i].distance = 0.0  # zero the distance for next iteration (because centroids may be further away)

    # calculate new centroids and set(or not) flag that shift is good enough
        for j in groups:
            _logger.info("Calculate new centroid")
            j.calc_new(DATA)
            j.set_flag(minimum)
            if j.flag == 1:
                flag += 1

    _logger.info("Done")

    # presentation of data
    clustered_docs = presentation.get_presentation(groups, DATA)
    _logger.info("Save clustered documents to output.txt")
    input_file = open('output.txt', 'w')
    for element in clustered_docs:
        input_file.write(str(element) + "\n")
    input_file.close()


def run():
    logging.basicConfig(filename='info.log', level=logging.INFO, stream=sys.stdout, filemode='w')
    main(sys.argv[1:])


if __name__ == "__main__":
    run()