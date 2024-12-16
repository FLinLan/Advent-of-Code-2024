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

def solve():
    # Read first part of the input and store in a set of tuples
    rules = set()
    while True:
        line = inp()
        if not line:
            break
        if '|' in line:
            a, b = map(int, line.split('|'))
            rules.add((a, b))
        else:
            break  # End of the first part

    # Read second part of the input line by line
    candidates = []
    while True:
        line = inp()
        if not line:
            break
        candidates.append(line.split(','))

    ans = 0
    print(candidates, rules)
    # Convert the lists of strings to integers
    for line in candidates:
        invalid_order = False
        N = len(line)
        for i in range(N-1):
            inversion = (int(line[i+1]), int(line[i]))
            if inversion in rules:
                invalid_order = True
        if not invalid_order:
            ans += int(line[N//2])

    # Output the results
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
