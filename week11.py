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
    visited[index] = True
    ls = [index]
    # print(chr(ord('A') + index), end=' ')

    next = index
    past = []
    past_ind = 0

    while True:
        now = next
        ls2 = []
        for j in range(len(graph)):
            if graph[now][j] == 1 and not visited[j]:
                # print(j, end=' ')
                visited[j] = True
                ls2.append(j)

        if len(ls2) == 0:
            if len(past[len(past) - 1]) == 0:
                if len(past) > 1:
                    past.pop(len(past) - 1)
                else:
                    break

            if past[len(past) - 1]:
                next = past[len(past) - 1][0]
                past[len(past) - 1].pop(0)
            else:
                break


        else:
            past.append(ls2)
            next = ls2[0]
            ls.extend(ls2)

        # print()

    for i in ls:
        print(chr(ord('A') + i), end=' ')


dfs(graph, 6, visited_dfs)
print()
bfs(graph, 4, visited_bfs)