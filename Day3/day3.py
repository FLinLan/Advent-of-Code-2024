#!/usr/bin/env python3
import sys
import re

# File I/O setup
sys.stdin = open('input2.txt', 'r')

def inp():
    return sys.stdin.read().strip()  # Read the entire input instead of one line

def solve():
    # Reading the entire input string
    line = inp()
    # Regex pattern to match valid mul(X,Y), do(), and don't()
    pattern = r"mul\(-?\d{1,3},-?\d{1,3}\)|do\(\)|don't\(\)"
    # Find all matches
    matches = re.findall(pattern, line)
    # Calculate the sum of the products for mul(X,Y)
    print(matches)
    ans = 0
    enabled = True
    for match in matches:
        if match == "don't()":
            enabled = False
        if match == "do()":
            enabled = True
        if match.startswith("mul(") and enabled:
            # Extract the numbers from the mul(X,Y) string
            numbers = re.findall(r"-?\d{1,3}", match)
            ans += int(numbers[0]) * int(numbers[1])

    print(ans)

def main():
    solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()
