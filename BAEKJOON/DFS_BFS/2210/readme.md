# 5x5 Grid

A 5x5 grid filled with random digits from 0 to 9.
When starting from a random point in this grid, you can move 5 times in either one of 4 directions including the previous direction location. Doing this will return a string of 6 digits such as '000000' or '121212'.

## Steps
1. Start → Initialize grid with random digits.
2. Choose Random Starting Point → (x, y) coordinates.
3. Call DFS Function → Parameters: (x, y, depth = 0, currentString = "").
    - In DFS:
    - Base case: If depth == 6, add currentString to set to ensure uniqueness and return.
    - Loop over 4 directions (up, down, left, right).
    - For each direction, if next position is valid, call DFS recursively with updated parameters.
4. Output count of unique strings.