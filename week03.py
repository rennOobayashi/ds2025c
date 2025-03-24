def inters(l1, l2):

    set1 = set(l1)
    set2 = set(l2)
    #set3 = set1.intersection(set2)

    #return list(set3)
    return list(set1 & set2)
    #return list(set1 - set2)
    #return list(set1 | set2)

l1 = [45, 1, 5, 4, 3, 21]
l2 = [2, 5, 45, 14, 11, 21, 35, 23]

l3 = inters(l1, l2)

print(l3)