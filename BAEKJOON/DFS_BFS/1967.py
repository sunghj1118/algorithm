import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

#take input and create graph of integers
n = int(input())
graph = [[] for _ in range(n+1)]

#dfs
def dfs(x, root):
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = root + b
            dfs(a, root+b)

#making tree
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

#finding node n1 farthest from starting node
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

#finding farthest node from our node n1 
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))