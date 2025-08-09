class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0

        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                i,j = rotten.popleft()
                
                for di,dj in directions:
                    ni,nj = i+di, j+dj
                    
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        rotten.append((ni,nj))
            
            minutes += 1
        
        return minutes if fresh==0 else -1