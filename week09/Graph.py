class MyGraph:
    def __init__(self, size):
        self._size = size

        self.graph = [[0 for _ in range(self._size)] for _ in range(self._size)]

G1 = MyGraph(4)

print(G1.graph)

# A = 0
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1

# B = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1

# C = 2
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1

# D = 3
G1.graph[3][0] = 1
G1.graph[0][2] = 1

print("G1 Undirected")
for row in G1.graph:
    for col in row:
        print(col, end=' ')

    print()
print()

G3 = MyGraph(4)

G3.graph[0][1] = 1
G3.graph[0][2] = 1

G3.graph[3][0] = 1
G3.graph[3][2] = 1

print("G3 directed")
for row in G3.graph:
    for col in row:
        print(col, end=' ')

    print()
print()

G5 = MyGraph(4)

G5.graph[0][3] = 1

G5.graph[1][2] = 1
G5.graph[1][3] = 1

G5.graph[2][1] = 1

G5.graph[3][0] = 1
G5.graph[3][1] = 1

print("G5 undirected")
for row in G5.graph:
    for col in row:
        print(col, end=' ')

    print()
print()

