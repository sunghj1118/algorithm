# 26169: Two Apples under Three Moves

This problem requires me to determine whether a student S can eat two apples under three moves when given a grid. 
Every time the student hops in the grid, the visited location becomes blocked by an obstacle, making it impossible to visit again.
The board is always of size 5x5.


## Approach
This is yet another DFS problem.
I will first take the input as a 2D array list.

Then I need to check if for each of the four directions: up, down, left, right; the student can move.
I need to initialize the move count and apple count every time before the student makes its first move.

