# creating first centroids

most_common = []

# zalozenie: rozumiem ze pierwsza wartosc w tupli to numbers a druga words??

n = 9  # number of centroids to create

for i in z:  # check all histograms
    if len(most_common) < n:  
        most_common.append(i)  # copy first histograms that will be soon replaced by better suited for the role of centroid 
    else:
        x, y = i.table[0]  # x - get the number of most commmon word used in this histogram
        j = 0 
        while j < n:  # go through out temporary "centroids" to check if this particular histogram is better suited than any temporary
            a, b = most_common[j].table[0]  # 
            if x > a:
                most_common[(j+1):len(most_common)] = most_common[j:(len(most_common)-1)]
                most_common[j] = i
                break  # it is better so end loop and get the next histogram
            else:
                j += 1


# now in most_common we have n histograms best suited for the role of centroid
# let's delete all words but the most common in each of histogram  
 
for i in range(len(most_common)):
    c = most_common[i]
    x, y = c.table[0]
    c.words = [y]
    c.numbers = [x]
    most_common[i] = c
