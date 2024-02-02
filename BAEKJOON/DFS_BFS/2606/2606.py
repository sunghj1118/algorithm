nodes = int(input())
edges = int(input())
graph = [[0] * (nodes + 1) for _ in range(nodes + 1)]
visited = [False] * (nodes + 1)
counter = [0]


def dfs(graph, v, visited, counter):
    visited[v] = True
    counter[0] += 1
    for i in range(1, len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited, counter)


for i in range(edges):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(graph, 1, visited, counter)
print(counter[0] - 1)
