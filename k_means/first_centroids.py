# creating first centroids from histograms with sorted (!) DATA


def create_first_centroids(number_of_groups, histograms):

    most_common = []  # create list of histograms best suited for being first centroids

    for i in histograms:  # check all histograms
        if len(most_common) < number_of_groups:
            # copy first histograms that will be soon replaced by better suited for the role of centroid
            most_common.append(i)
        else:
            # get the number and the name of most common word used in this (already sorted) histogram
            number, word = i.table[0]
            j = 0
            # go through out temporary "centroids"
            while j < number_of_groups:
                # to check if this particular histogram is better suited than any temporary
                temp_number, temp_word = most_common[j].table[0]  #
                if number > temp_number:
                    # shift the list
                    most_common[(j+1):len(most_common)] = most_common[j:(len(most_common)-1)]
                    # and add the new temp histogram on appropriate position
                    most_common[j] = i
                    break  # it is placed on list so end loop and check the next histogram
                else:
                    j += 1

    # now in most_common we have number_of_groups histograms best suited for the role of centroid
    # let's copy each histogram so that we don't change anything in it
    # and delete all words but the most common in each copy

    for i in range(len(most_common)):
        copied_histogram = most_common[i]
        number, value = copied_histogram.table[0]
        copied_histogram.words = [value]
        copied_histogram.numbers = [number]
        most_common[i] = copied_histogram

    return most_common
