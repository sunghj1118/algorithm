def time_for_cheese_to_melt(grid):
    # basecase
    if not grid or not grid[0]:
        return 0
    
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    time = 0
    
    def iter_dfs():
        stack = [(0,0)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        
        
        while stack:
            x,y = stack.pop()
            grid[x][y] = -1 # visited air

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                # check if within bounds, not visited, and air
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] == 0:
                    stack.append((nx,ny))
                    visited[nx][ny] = True


    def melt_cheese():
        melted = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    air_contact = sum(1 for dx,dy in directions if 0 <= i+dx < n and 0 <= j+dy < m and grid[i+dx][j+dy] == -1)

                    if air_contact >= 2:
                        grid[i][j] = 2 # mark for melting
                        melted = True
        
        return melted

    
    while True:
        # mark all reachable air as -1
        iter_dfs()

        # melt cheese
        if not melt_cheese():
            break

        # update grid and reset air
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                elif grid[i][j] == -1:
                    grid[i][j] = 0
        
        time += 1
    
    return time
    

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(time_for_cheese_to_melt(grid))