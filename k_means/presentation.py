# presentation of DATA


def get_presentation(groups, DATA):
    # iterate as many times as many groups we have created
    for i in groups:
        print "Group: "
        # go through all probes
        for j in DATA:
            # if this probe belongs to this group
            if j.group == i.number:
                # print the path to this probe's histogram
                print j.data.doc_name
                # so that we know to which group it belonged to at the beginning
