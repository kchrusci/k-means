# presentation of DATA


def get_presentation(groups, DATA):
    # iterate as many times as many groups we have created
    doc_names = []
    group_number = 0
    for i in groups:
        group_number += 1
        group_name = "Group: " + str(group_number)
        # go through all probes
        for j in DATA:
            # if this probe belongs to this group
            if j.group == i.number:
                # print the path to this probe's histogram
                doc_names.append((group_name, j.doc_name))
                # so that we know to which group it belonged to at the beginning
    return doc_names
