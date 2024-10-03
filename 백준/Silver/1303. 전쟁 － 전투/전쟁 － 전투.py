def power_levels(grid, width, height):
    # Base case
    if not grid or not grid[0]:
        return "0 0"

    # Visited array
    visited = [[False for _ in range(width)] for _ in range(height)]
    white_power = 0
    blue_power = 0
    
    def iter_dfs(x, y, char):
        stack = [(x, y)]
        area = 0

        while stack:
            curr_x, curr_y = stack.pop()  # curr_x is column, curr_y is row

            # If not out of bounds, not visited, and desired char
            if 0 <= curr_y < height and 0 <= curr_x < width and not visited[curr_y][curr_x] and grid[curr_y][curr_x] == char:
                visited[curr_y][curr_x] = True
                area += 1
                # Add neighboring cells to the stack
                stack.extend([(curr_x + 1, curr_y), (curr_x - 1, curr_y), (curr_x, curr_y + 1), (curr_x, curr_y - 1)])

        return area

    for y in range(height):  # Iterate over rows (height)
        for x in range(width):  # Iterate over columns (width)
            if not visited[y][x]:  # Check if cell is unvisited
                if grid[y][x] == 'W':
                    power = iter_dfs(x, y, 'W')
                    white_power += power * power
                elif grid[y][x] == 'B':
                    power = iter_dfs(x, y, 'B')
                    blue_power += power * power
    
    return f"{white_power} {blue_power}"

# Input handling
n, m = map(int, input().split())  # n is width (columns), m is height (rows)
grid = [list(input().strip()) for _ in range(m)]  # Read m rows of input
print(power_levels(grid, n, m))