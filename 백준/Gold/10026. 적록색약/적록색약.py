def numAreas(grid):
    # base case
    if not grid:
        return "0 0"
    
    rows, cols = len(grid), len(grid[0])
    healthy_visited = [[False for _ in range(cols)] for _ in range(rows)]
    blind_visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    blind = 0
    healthy = 0

    def iter_dfs(start_i, start_j, char, visited, is_blind):
        stack = [(start_i, start_j)]

        while stack:
            i,j = stack.pop()
        
            # out of bounds, already visited, or char mismatch
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j]:
                continue
        
            # for blind person, treat 'R' and 'G' as the same
            current_char = grid[i][j]
            if is_blind and current_char in ['R', 'G']:
                current_char = 'RG'

            # check if the current cell matches the area we're exploring
            # if not blind, then check if identical
            # if blind, check if identical and either RG
            if (is_blind and char == 'RG' and current_char != 'RG') or \
                (is_blind and char != 'RG' and current_char != char) or \
                (not is_blind and current_char != char):
                continue

            visited[i][j] = True

            # check all 4 directions
            stack.append((i+1, j))
            stack.append((i-1, j))
            stack.append((i, j+1))
            stack.append((i, j-1))

    for i in range(rows):
        for j in range(cols):
            # 아직 탐색 안해봤으면
            if not healthy_visited[i][j]:
                iter_dfs(i, j, grid[i][j], healthy_visited, False)
                healthy += 1

    for i in range(rows):
        for j in range(cols):
            # 아직 탐색 안해봤으면
            if not blind_visited[i][j]:
                char = 'RG' if grid[i][j] in ['R', 'G'] else grid[i][j]
                iter_dfs(i, j, char, blind_visited, True)
                blind += 1

    return f"{healthy} {blind}"


n = int(input()) # num rows
grid = []
for _ in range(n):
    row = list(str(input()))
    grid.append(row)

print(numAreas(grid))