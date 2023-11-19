# 26169: Two Apples under Three Moves

This problem requires me to determine whether a student S can eat two apples under three moves when given a grid. 
Every time the student hops in the grid, the visited location becomes blocked by an obstacle, making it impossible to visit again.
The board is always of size 5x5.


## Approach
This is yet another DFS problem.
I will first take the input as a 2D array list.

Then I need to check if for each of the four directions: up, down, left, right; the student can move.
I need to initialize the move count and apple count every time before the student makes its first move.

# Planning
I thought about how to solve this problem a little more.

1. Initialize: Set up the board and initial position.
2. DFS Function: The DFS function needs to avoid visiting the same cell since that would be equivalent to encountering an obstacle.
3. Check for apples: Check if the cell is an apple or obstacle. The function should return true if two apples are eaten within three moves, else false.
4. Stopping conditions: If the move count exceeds 3 or finds 2 apples, the search stops.
5. Path traversal: explore all 4 directions of the starting position.
6. Backtracking: After visiting a cell, we mark it as visited to prevent revisiting. Once all paths from that cell are explored, we backtrack and mark it as unvisited for the other paths.