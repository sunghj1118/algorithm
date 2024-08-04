import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)] # up, down, left, right
        queue = deque([(entrance[0], entrance[1], 0)]) # row, col, steps
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            row, col, steps = queue.popleft()

            
            # explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # check if new position is valid and not a wall
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                    # check if it's an exit but not the entrance
                    if (new_row == 0 or new_row == rows-1 or new_col == 0 or new_col == cols-1):
                        return steps+1
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps+1))
 
        return -1