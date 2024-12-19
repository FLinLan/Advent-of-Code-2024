#!/usr/bin/env python3
import sys
from typing import Dict

# File I/O setup
sys.stdin = open('input1.txt', 'r')

def inp():
    return sys.stdin.readline().strip()


def solve():
    # Reading input string
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            grid.append(list(line))
    print(grid)
    ROWS, COLS = len(grid), len(grid[0])

    start, end = [], []
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 'S':
                start = [r, c]
            if grid[r][c] == 'E':
                end = [r, c]

    # starting at 'S', do a graph traversal until reaching E 
    # grid dp
    # 

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
