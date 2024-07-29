from collections import deque

def count_grass_clumps(grid):
    R = len(grid)
    C = len(grid[0])
    visited = [[False for _ in range(C)] for _ in range(R)]
    clump_count = 0

    def bfs(row, col):
        queue = deque([(row, col)])
        visited[row][col] = True
        
        while queue:
            r, c = queue.popleft()
            
            # Check adjacent cells (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '#' and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                clump_count += 1

    return clump_count

r, c = map(int, input().split())
rows = []
for i in range(r):
	rows.append(list(input()))

print(count_grass_clumps(rows))