#!/usr/bin/env python3
import sys
from collections import deque

# File I/O setup
sys.stdin = open('input1.txt', 'r')

def isValid(r, c, ROWS, COLS, visit):
    return (r, c) not in visit and 0 <= r < ROWS and 0 <= c < COLS

def matrixBFS(grid, sr, sc, visit):
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque([(grid[sr][sc], sr, sc)])
    visit = set([(sr, sc)])
    peaks = 0

    while q:
        height, r, c = q.popleft()
        # If we reach a height of 9, count it as a peak
        if height == 9:
            peaks += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if isValid(nr, nc, ROWS, COLS, visit) and grid[nr][nc] == height + 1:
                q.append((grid[nr][nc], nr, nc))
                visit.add((nr, nc))

    return peaks

def solve():
    # Reading input grid
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            grid.append([int(ch) for ch in line])

    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    ans = 0

    # Perform BFS for each trailhead (starting at height 0)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0 and (r, c) not in visit:
                ans += matrixBFS(grid, r, c, visit)

    print(ans)

def main():
    solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()