import sys

sys.setrecursionlimit(10 ** 6)

# Read input
N, M = map(int, input().split())
bessieGrid = [[0] * N for _ in range(N)]  # save bessie's moving time grid
elsieGrid = [[0] * N for _ in range(N)]  # save elsie's moving time grid

for _ in range(M):
    x, y, bessie, elsie = map(int, input().split())  # save input data

    # x and y are the numbers of the connected pastures
    x -= 1
    y -= 1

    # bessie and elsie are the time it takes to move from pasture x to pasture y
    bessieGrid[x][y] = bessie
    elsieGrid[x][y] = elsie


def dfs(graph, dist, curr_node, curr_dist):
    if curr_node == n - 1:
        dist[curr_dist] = True
        return

    for a in range(curr_node + 1, n):
        if graph[curr_node][a] > 0:
            dfs(graph, dist, a, curr_dist + graph[curr_node][a])


# 가능한 이동 시간을 나타내는 불리언 배열
# bessieCan은 Bessie가 각 가능한 이동 시간에 도달할 수 있는지 여부 저장, elsieCan은 Elsie가 각 가능한 이동 시간에 도달할 수 있는지 여부 저
bessieCan = [False] * 20000
elsieCan = [False] * 20000

dfs(bessieGrid, bessieCan, 0, 0)
dfs(elsieGrid, elsieCan, 0, 0)

# 초기에 best 변수를 무한대 값으로 설정. 이 변수는 Bessie와 Elsie가 동시에 이동할 수 있는 최적의 이동 시간
best = float('inf')

for i in range(len(bessieCan)):
    if bessieCan[i] and elsieCan[i]:
        best = i
        break

# best가 여전히 무한대 값인 경우 "IMPOSSIBLE"을 출력하고, 그렇지 않으면 최적의 이동 시간을 출력
if best == float('inf'):
    print("IMPOSSIBLE")
else:
    print(best)
