#!/usr/bin/env python3
import sys
from typing import Dict

# File I/O setup
sys.stdin = open('input2.txt', 'r')

def inp():
    return sys.stdin.readline().strip()

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
