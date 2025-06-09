from signal import valid_signals

items, kgs = input().split()
items = int(items)
kgs = int(kgs)
isCan = True

if not(0 <= items <= 1000):
    isCan = False
elif not(1 <= kgs <= 100000):
    isCan = False

ks = []
vs = []

if isCan:
    for _ in range(items):
        k, v = input().split()
        k = int(k)
        v = int(v)

        if k <= kgs and  1 <= v <= 1000:
            ks.append(k)
            vs.append(v)
        else:
            ks.append(0)
            vs.append(0)

    performance = vs[0]

    for i in range(items):
        if vs[i] > performance:
            performance = vs[i]

        for j in range(items):
            if j == i:
                continue

            sumit = vs[i] + vs[j]

            if performance < sumit and (ks[i] + ks[j]) <= kgs:
                performance = sumit

    print(performance)