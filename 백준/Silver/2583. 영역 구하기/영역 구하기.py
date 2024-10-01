def dfs(grid):
    # base case
    if not grid or not grid[0]:
        return 0
    
    # visited
    visited = [[False for _ in range(n)] for _ in range(m)]
    uncolored_count = 0
    areas = []

    def iter_dfs(i,j):
        stack = [(i,j)]
        area = 0
        while stack:
            x,y = stack.pop()

            # if not outofbounds, not visited, and clean
            if 0 <= x < m and 0 <= y < n and not visited[x][y]\
                and grid[x][y] == 0:
                visited[x][y] = True
                area += 1
                stack.extend([(x-1,y), (x+1,y), (x,y-1), (x,y+1)])
        
        return area
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not visited[i][j]:
                uncolored_count += 1
                area = iter_dfs(i,j)
                areas.append(area)
    
    
    return uncolored_count, sorted(areas)



m,n,k = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for i in range(right_y-left_y):
        for j in range(right_x-left_x):
            grid[left_y+i][left_x+j] = 1

uncolored, areas = dfs(grid)
print(uncolored)
print(' '.join(map(str,areas)))