class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            local_perimiter = 0

            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc

                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==0:
                            local_perimiter+=1
                        elif grid[nr][nc]==1 and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                    else:
                        local_perimiter+=1
            
            return local_perimiter


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return bfs(i,j)

        return 0