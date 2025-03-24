def inters(l1, l2):
    l3 = []

    #l3 = [v for v in l1  if v in l2]
    for v in l1:
        if v in l2:
            l3.append(v)

    return l3

l1 = [45, 1, 5, 4, 3, 21]
l2 = [2, 5, 45, 14, 11, 21, 35, 23]

l3 = inters(l1, l2)

print(l3)