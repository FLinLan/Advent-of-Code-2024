#!/usr/bin/env python3
import sys
from typing import Dict

# File I/O setup
sys.stdin = open('input2.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def inp():
    return sys.stdin.readline().strip()

def dp(current, target, i, nums, cache) -> bool:
    if current > target or i >= len(nums):
        # print(f"Match found: current={current}, target={target}")
        return current == target  # Check if the current value equals the target
    if (current, i) in cache:
        return cache[(current, i)]

    plus = dp(current + nums[i], target, i+1, nums, cache)
    multiply = dp(current * nums[i], target, i+1, nums, cache)
    concat = dp(int(str(current) + str(nums[i])), target, i+1, nums, cache)

    cache[(current, i)] = plus or multiply or concat
    return cache[(current, i)]

def isValid(r, c, ROWS, COLS) -> bool:
    return 0 <= r < ROWS and 0 <= c < COLS

def solve():
    grid = []
    while True:
        row_arr = inp()
        if not row_arr:
            break
        grid.append(list(row_arr))

    # Output the results
    ROWS, COLS = len(grid), len(grid[0])

    """
    the same frequency implies that two of the same letter is on the same line (same slope)
    how do we decide the number of points we should add to the grid?
    letters and chars have a higher precedence than the anti nodes (won't be overwritten)
    check for each line on the grid, diagonal, vertical, horizontal reverse diagonal
    use a hash table to check if two of the same symbol have the same "slope"
    """
    for r in range(ROWS):
        for c in range(COLS):



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