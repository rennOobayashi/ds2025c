class MyGraph:
    def __init__(self, size):
        self._size = size

        self.graph = [[0 for _ in range(self._size)] for _ in range(self._size)]

    def getSize(self):
        return self._size

a = 0
b = 1
c = 2
d = 3
nameArr = ['a', 'b', 'c', 'd']

G1 = MyGraph(4)

print(G1.graph)

# A = 0
G1.graph[a][b] = 1
G1.graph[a][c] = 1
G1.graph[a][d] = 1

# B = 1
G1.graph[b][a] = 1
G1.graph[b][c] = 1

# C = 2
G1.graph[c][a] = 1
G1.graph[c][b] = 1
G1.graph[c][d] = 1

# D = 3
G1.graph[d][a] = 1
G1.graph[d][c] = 1

print("G1 Undirected")

print(end='  ')
for i in nameArr:
    print(i, end=' ')
print()

cnt = 0
for row in G1.graph:
    print(nameArr[cnt], end=' ')
    for col in row:
        print(col, end=' ')

    cnt += 1

    print()
print()

G3 = MyGraph(4)

G3.graph[a][b] = 1
G3.graph[a][c] = 1

G3.graph[d][a] = 1
G3.graph[d][c] = 1

print("G3 directed")

print(end='  ')
for i in nameArr:
    print(i, end=' ')
print()

cnt = 0
for row in G3.graph:
    print(nameArr[cnt], end=' ')
    for col in row:
        print(col, end=' ')

    cnt += 1

    print()
print()

# no selft
G5 = MyGraph(4)

G5.graph[a][d] = 1

G5.graph[b][c] = 1
G5.graph[b][d] = 1

G5.graph[c][b] = 1

G5.graph[d][a] = 1
G5.graph[d][b] = 1


print("G5 undirected")

print(end='  ')
for i in nameArr:
    print(i, end=' ')
print()

cnt = 0
for row in G5.graph:
    print(nameArr[cnt], end=' ')
    for col in row:
        print(col, end=' ')

    cnt += 1

    print()
print()

