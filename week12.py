from collections import deque

graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]

com_ls = []

#depth first search
def dfs(graph, index, visited):
    visited[index] = True
    print(chr(ord('A') + index), end=' ')

    for j in range(len(graph)):
        if graph[index][j] == 1 and not visited[j]:
            dfs(graph, j, visited)

#breadth first search
def bfs(graph, index, visited):
    q = deque([index])
    visited[index] = True

    while q:
        i = q.popleft()
        print(chr(ord('A') + i), end=' ')

        for j in range(len(graph)):
            if graph[i][j] == 1 and not visited[j]:
                q.append(j)
                visited[j] = True



dfs(graph, 4, visited_dfs)
print()
bfs(graph, 4, visited_bfs)