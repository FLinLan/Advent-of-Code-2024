#!/usr/bin/env python3
import sys
import math
from typing import List

# File I/O setup
sys.stdin = open('input2.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def inp():
    return sys.stdin.readline().strip()

def iinp():
    return int(inp())

def linp():
    return list(map(int, inp().split()))

def isValid(r, c, ROWS, COLS) -> bool:
    return 0 <= r < ROWS and 0 <= c < COLS

def solve():
    # Read in the input grid
    grid = []
    while True:
        row_arr = inp()
        if not row_arr:
            break
        grid.append(list(row_arr))

    # Output the results
    ROWS, COLS = len(grid), len(grid[0])

    # Find starting position
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '^':
                sr, sc = r, c

    # run a simulation through the path
    visit = set([(sr, sc)])  # Include starting position
    states = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left

    r, c = sr, sc
    index = 0  # Start moving up

    while True:
        dr, dc = states[index]
        nr, nc = r + dr, c + dc

        # Check if guard would leave the mapped area
        if not isValid(nr, nc, ROWS, COLS):
            break

        if grid[nr][nc] != '#':
            r, c = nr, nc  # Move to new position
            visit.add((r, c))
        else:
            # Hit a wall, turn right
            index = (index + 1) % 4

    print(len(visit))

def main():
    # For single test case
    solve()
    # Uncomment below for multiple test cases
    # t = iinp()
    # for _ in range(t):
    #     solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()
        sys.stdout.close()
