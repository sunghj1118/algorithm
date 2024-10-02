def largest_area(grid):
    # base case
    if not grid or not grid[0]:
        return 0
    
    # visited
    visited = [[False for _ in range(m)] for _ in range(n)]
    painting_count = 0
    max_area = 0

    def iter_dfs(i,j):
        stack = [(i,j)]
        area = 0
        while stack:
            x,y = stack.pop()

            # if not outofbounds, not visited, and drawing
            if 0 <= x < n and 0 <= y < m and not visited[x][y] \
            and grid[x][y] == 1:
                visited[x][y] = True
                area += 1
                stack.extend([(x-1,y), (x+1,y), (x,y-1), (x,y+1)])
        
        return area
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                painting_count += 1
                area = iter_dfs(i,j)
                max_area = max(max_area, area)
    return painting_count, max_area

n,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
painting_count, max_area = largest_area(grid)
print(painting_count)
print(max_area)