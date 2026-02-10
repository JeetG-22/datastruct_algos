"""
Count the unique paths from top left to bottom right. A single path may only move along 0s and can't visit the same cell
more than once
"""
matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()

def dfs(grid, r, c, visited):
    ROW, COL= len(grid), len(grid[0])
    
    """
    Base Case Conditions:
    1) either the column or row is smaller than the 0 bounds
    2) either column or row is bigger than the grid bounds
    3) the grid point is already in the visited set
    4) the grid point isn't a valid location to move towards
    """

    if min(r, c) < 0 or r == ROW or c == COL or (r,c) in visited or grid[r][c] == 1:
        return 0
    if r == ROW - 1 and c == COL - 1: #it reached the bottom right corner
        return 1
    
    #add to visited before going onto the next dir
    visited.add((r,c))

    count = 0 #count the number of paths
    count += dfs(grid, r + 1, c, visited)
    count += dfs(grid, r - 1, c, visited)
    count += dfs(grid, r, c + 1, visited)
    count += dfs(grid, r, c - 1, visited)

    visited.remove((r,c)) #for backtracking purposes
    return count


print(f"Number of Unique Paths: {dfs(matrix, 0, 0, set())}")

        


