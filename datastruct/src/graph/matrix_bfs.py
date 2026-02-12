from collections import deque
"""
Get the length of shortest path from top left to bottom right
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

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
        return -1

    q = deque()
    visited = set()
    q.append((0,0))
    visited.add((0,0))
    dir = [(0,1), (1,0), (-1, 0), (0,-1)]
    length = 0

    while q:
        for _ in range(len(q)):
            r,c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1: #before the 3rd loop because its the length at that current layer
                return length
            for dr,dc in dir:
                row, col = r + dr, c + dc
                if min(row,col) < 0 or row >= ROWS or col >= COLS or (row,col) in visited or grid[row][col] == 1:
                    continue
                q.append((row,col))
                visited.add((row,col))
        length += 1

print(bfs(matrix))

            
                


    
