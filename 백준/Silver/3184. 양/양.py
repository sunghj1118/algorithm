import sys
input = sys.stdin.readline

def dfs(grid):
    # basecase
    if not grid or not grid[0]:
        return 0,0
    
    # visited
    visited = [[False for _ in range(m)] for _ in range(n)]
    total_wolves, total_sheep = 0,0
    
    def iter_dfs(i,j):
        nonlocal wolves, sheep
        stack = [(i,j)]

        while stack:
            x,y = stack.pop()

            if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] in ['.', 'v', 'o']:
                visited[x][y] = True
                stack.extend([(x+1, y), (x-1,y), (x,y+1), (x,y-1)])
                
                if grid[x][y] == '.':
                    continue
                elif grid[x][y] == 'v':
                    wolves += 1
                else:
                    sheep += 1
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '#' and not visited[i][j]:
                wolves, sheep = 0,0
                iter_dfs(i,j)
                if wolves < sheep:
                    total_sheep += sheep
                else:
                    total_wolves += wolves
                    

    return total_sheep, total_wolves

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

print(*dfs(grid))