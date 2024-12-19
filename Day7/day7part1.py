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
        return current == target  # Check if the current value equals the target
    if (current, i) in cache:
        return cache[(current, i)]

    plus = dp(current + nums[i], target, i+1, nums, cache)
    multiply = dp(current * nums[i], target, i+1, nums, cache)
    concat = dp(int(str(current) + str(nums[i])), target, i+1, nums, cache)

    cache[(current, i)] = plus or multiply or concat
    return cache[(current, i)]

def solve():
    equations = []
    for line in sys.stdin:
        # Split the line by the colon
        parts = line.split(':')
        if len(parts) > 1:
            key = int(parts[0].strip())                # Number before the colon
            numbers = list(map(int, parts[1].split()))  # Numbers after the colon
            equations.append([key] + numbers)           # Combine them in a single array

    ans = 0

    for line in equations:
        cache = dict()
        current, target = line[1], line[0]
        nums = line[2:]
        if dp(current, target, 0, nums, cache):
            ans += target  # Add the target value if the equation is valid

    print(ans)

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