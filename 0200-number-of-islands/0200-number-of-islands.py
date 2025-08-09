class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i,j):
            q = deque()
            visited.add((i,j))
            q.append((i,j))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            while q:
                r,c = q.popleft()
                
                for d in directions:
                    nr,nc = r+d[0], c+d[1]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        
        return islands