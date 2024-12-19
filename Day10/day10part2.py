#!/usr/bin/env python3
import sys

# File I/O setup
sys.stdin = open('input1.txt', 'r')

def isValid(r, c, ROWS, COLS, visit):
    """Check if a position is within bounds and not yet visited."""
    return (r, c) not in visit and 0 <= r < ROWS and 0 <= c < COLS

def dfs(grid, r, c, visit, path, trails):
    """Recursive DFS to explore distinct decreasing trails."""
    ROWS, COLS = len(grid), len(grid[0])
    visit.add((r, c))
    path.append((r, c))

    extended = False
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if isValid(nr, nc, ROWS, COLS, visit) and grid[nr][nc] < grid[r][c]:
            dfs(grid, nr, nc, visit, path, trails)
            extended = True

    if not extended:
        trails.add(tuple(path))

    path.pop()
    visit.remove((r, c))

def count_distinct_trails(grid, sr, sc):
    """Count distinct decreasing trails starting from (sr, sc)."""
    trails = set()
    visit = set()
    dfs(grid, sr, sc, visit, [], trails)
    return len(trails)

def solve():
    # Reading input grid
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            grid.append([int(ch) for ch in line])

    ROWS, COLS = len(grid), len(grid[0])
    total_rating = 0

    # Perform DFS for each trailhead (starting at height 0)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                total_rating += count_distinct_trails(grid, r, c)

    print(total_rating)

def main():
    solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()