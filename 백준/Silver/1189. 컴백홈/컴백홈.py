import sys
input = sys.stdin.readline


r,c,k = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0

def dfs(x,y,distance):
    global answer

    # check if destination reached
    if distance == k and x == 0 and y == c-1:
        answer += 1
    else:
        # mark current as visited
        original = graph[x][y]
        graph[x][y] = 'T'

        # explore all four directions
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                dfs(nx,ny,distance+1)
        
        # backtrack : restore original state
        graph[x][y] = original

# start DFS from bottom left corner
dfs(r-1,0,1)

# print result
print(answer)