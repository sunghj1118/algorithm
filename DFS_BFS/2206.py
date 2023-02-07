from collections import deque

n, m = map(int, input().split())
graph = []

#3d array to see if wall is broken
#[x][y][1] means broken while [x][y][0] means not broken
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

#4 possible directions
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        #if we arrive to the end return distance
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #if the next move is a wall and we didnt break it
            if graph[nx][ny] == 1 and c ==0:
                visited[nx][ny][1] = visited[a][b][0] +1
                queue.append((nx, ny, 1))
            #if the next move isnt a wall and we havent visited it
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1

print(bfs(0,0,0))