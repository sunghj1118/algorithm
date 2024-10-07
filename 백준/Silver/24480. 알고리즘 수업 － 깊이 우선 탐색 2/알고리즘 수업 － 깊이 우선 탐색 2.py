import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(v):
    global order_count
    visited[v] = True
    order_count += 1
    order[v] = order_count
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)
    
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [False] * (n+1)
order = [0] * (n+1)
order_count = 0

dfs(r)

for i in range(1, n+1):
    print(order[i])