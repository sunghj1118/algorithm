def find_letters(grid):
    # basecase
    if not grid or not grid[0]:
        return 0
    
    # visited
    n,m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    letters = 0

    def iter_dfs(i,j):
        stack = [(i,j)]

        while stack:
            x,y = stack.pop()

            # if withinbounds, not visited, and val is 1
            if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] == 1:
                visited[x][y] = True
                stack.extend([(x-1,y), (x+1,y), (x,y-1), (x,y+1), (x-1,y-1), (x-1,y+1), (x+1, y-1), (x+1, y+1)])
            

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                iter_dfs(i,j)
                letters += 1
    
    return letters

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(find_letters(grid))