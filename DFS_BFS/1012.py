from collections import deque

#down,up,left,right directions
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#take input and create graph of integers
T = int(input())

def BFS(graph, x, y):
    #changing graph to 0 once visited
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()
        #checking directions
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

#for T instances run for loop
for i in range(T):
    count = 0
    N, M, K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                BFS(graph, x,y)
                count += 1
    
    print(count)

