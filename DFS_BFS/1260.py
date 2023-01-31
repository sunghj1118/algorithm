from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visitlist1[v] = 1
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visitlist1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visitlist1[i] = 1

                


n, m, v = map(int, read().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visitlist1 = [0] * (n+1)
visitlist2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

bfs(v)