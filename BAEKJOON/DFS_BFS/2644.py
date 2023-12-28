# get input
# first input is the number of people
# second input is the number of the first person and the second person
# third input is the number of the relationships
# fourth input and so on are the relationships between people
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []


# create graph showing how the nodes are connected in a 2d array
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# dfs function


def dfs(v, num):
    num += 1
    visited[v] = True

    if v == B:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(A, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
