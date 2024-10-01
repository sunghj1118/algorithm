def safeAreas(grid, rain):
    # base case
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    safe_regions = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def iter_dfs(start_i, start_j):
        stack = [(start_i, start_j)]

        while stack:
            i,j = stack.pop()

            # out of bounds
            if i < 0 or i >= rows or j >= cols or j < 0:
                continue
            
            visited[i][j] = True

            # check four directions    
            for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            # add unvisited and sinking tiles to stack
                if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] \
                and grid[ni][nj] > rain:
                    stack.append((ni,nj))
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] > rain:
                iter_dfs(i,j)
                safe_regions += 1


    return safe_regions


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in grid)
max_areas = 0

for rain in range(max_height):
    max_areas = max(max_areas, safeAreas(grid, rain))

print(max_areas)