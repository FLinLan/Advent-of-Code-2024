#!/usr/bin/env python3
import sys

# File I/O setup
sys.stdin = open('in5.txt', 'r')

def inp():
    return sys.stdin.readline().strip()

def isValid(r, c, ROWS, COLS):
    return 0 <= r < ROWS and 0 <= c < COLS

def validPattern(r, c, ROWS, COLS, grid):
    if not isValid(r+2, c+2, ROWS, COLS): return False
    first = (grid[r][c] == 'M' and grid[r][c+2] == 'M' and grid[r+1][c+1] == 'A' and grid[r+2][c] == 'S' and grid[r+2][c+2] == 'S')
    second = (grid[r][c] == 'M' and grid[r][c+2] == 'S' and grid[r+1][c+1] == 'A' and grid[r+2][c] == 'M' and grid[r+2][c+2] == 'S')
    third = (grid[r][c] == 'S' and grid[r][c+2] == 'M' and grid[r+1][c+1] == 'A' and grid[r+2][c] == 'S' and grid[r+2][c+2] == 'M')
    fourth = (grid[r][c] == 'S' and grid[r][c+2] == 'S' and grid[r+1][c+1] == 'A' and grid[r+2][c] == 'M' and grid[r+2][c+2] == 'M')

    return first or second or third or fourth


def solve():
    # Reading the grid of characters
    grid = []

    for line in sys.stdin:
        line = line.strip()
        if line:
            grid.append(list(line))  # Convert each line into a list of characters
    print(grid)

    ans = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if validPattern(r, c, ROWS, COLS, grid):
                ans += 1
    print(ans)

def main():
    # For single test case
    solve()
    # Uncomment below for multiple test cases
    # t = int(inp())
    # for _ in range(t):
    #     solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()
