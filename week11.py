graph = [0, 0, 0, 0, 0, 0, 0, 0]

visited_gfs = [0 for _ in range(len(graph))]

def gfs(graph, index, visited):
    visited[index] = 1
    print(chr(ord('A') + index), end='')


gfs(graph, 0, visited_gfs)