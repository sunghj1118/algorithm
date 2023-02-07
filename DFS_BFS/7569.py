from collections import deque

# six possible directions
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

#m length, n width, h height
m, n, h = map(int, input().split())
graph = []
queue = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k]==1:
                queue.append([i,j,k])
    graph.append(temp)

while(queue):
    x,y,z = queue.popleft()

    #check directions
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c] == 0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z] + 1

days = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        days = max(days, max(j))
print(days-1)