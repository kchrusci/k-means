
# presentation of DATA

for i in groups:  # iterate as many times as many groups we have created
    print "Group: "
    for j in DATA:  # go through all probes
        if j.group == i.number  # if this probe belongs to this group
            print j.data.doc_name  # print the path to this probe's histogram -> we know to which group it belonged at the beginning
    
