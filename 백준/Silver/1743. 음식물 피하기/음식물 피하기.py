def max_garbage(grid):
    # basecase
    if not grid or not grid[0]:
        return 0

    # visited
    visited = [[False for _ in range(m)] for _ in range(n)]
    largest = 0

    def iter_dfs(i,j):
        stack = [(i,j)]
        area = 0
        while stack:
            x,y = stack.pop()

            # if not outofbounds, not visited, and garbage
            if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] == 1:
                visited[x][y] = True
                area += 1
                stack.extend([(x-1,y), (x+1,y), (x,y-1), (x,y+1)])
        
        return area
    
    for i in  range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                area = iter_dfs(i,j)
                largest = max(largest, area)
    

    return largest

n,m,k = map(int, input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    x,y = map(int, input().split())
    grid[x-1][y-1] = 1

print(max_garbage(grid))