graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

visited_gfs = [False for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]

def gfs(graph, index, visited):
    pass

def bfs(graph, index, visited):
    pass

gfs(graph, 6, visited_gfs)
print()
bfs(graph, 6, visited_bfs)