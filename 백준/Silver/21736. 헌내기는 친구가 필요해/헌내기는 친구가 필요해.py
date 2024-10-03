def find_friends(grid):
    # basecase
    if not grid or not grid[0]:
        return 0
    
    # visited
    visited = [[False for _ in range(m)] for _ in range(n)]

    def iter_dfs(i,j):
        stack = [(i,j)]
        friend_count = 0

        while stack:
            x,y = stack.pop()

            # if not outofbounds, not visited and desired char
            if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] in ['P', 'O', 'I']:
                visited[x][y] = True
                if grid[x][y] == 'P':
                    friend_count += 1
                stack.extend([(x+1,y), (x-1,y), (x,y+1), (x,y-1)])
            
        return friend_count

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'I':
                friend_count = iter_dfs(i,j)

    return friend_count

n,m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
result = find_friends(grid)

if result > 0:
    print(result)
else:
    print('TT')