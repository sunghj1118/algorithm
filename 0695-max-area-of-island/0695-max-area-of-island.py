class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r,c):
            q = deque()
            island_size = 1

            q.append((r,c))
            visited.add((r,c))

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        island_size += 1
            
            return island_size

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, bfs(i,j))

        return max_area