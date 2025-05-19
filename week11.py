graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

visited_gfs = [False for _ in range(len(graph))]

def gfs(graph, index, visited):
    visited[index] = True
    print(chr(ord('A') + index), end='')

    for j in range(len(graph)):
        if graph[index][j] == 1 and not visiited[j]:
            gfs(graph, j, visited)

gfs(graph, 6, visited_gfs)