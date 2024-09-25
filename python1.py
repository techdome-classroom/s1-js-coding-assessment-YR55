def count_islands(grid):
    # Function to mark the connected land ('L') as visited
    def mark_island_visited(grid, i, j, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 'W':
            return
        # Mark the land 'L' as visited by setting it to 'W'
        grid[i][j] = 'W'
        # Recursively visit all connected land horizontally and vertically
        mark_island_visited(grid, i - 1, j, rows, cols)  # Up
        mark_island_visited(grid, i + 1, j, rows, cols)  # Down
        mark_island_visited(grid, i, j - 1, rows, cols)  # Left
        mark_island_visited(grid, i, j + 1, rows, cols)  # Right

    # Getting the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    # Looping through the grid to find islands
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L':
                # Found an island
                island_count += 1
                # Mark the entire island as visited
                mark_island_visited(grid, i, j, rows, cols)

    return island_count

# Input as given in the first example
grid1 = [
    ['L', 'L', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W']
]

# Input as given in the second example
grid2 = [
    ['L', 'L', 'W', 'W', 'W'],
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'L']
]

# Output for both inputs
print(count_islands(grid1))  # Output: 1
print(count_islands(grid2))  # Output: 3