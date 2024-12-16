#!/usr/bin/env python3
import sys
import math
from typing import List

# File I/O setup
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def inp(): 
    return sys.stdin.readline().strip()

def iinp(): 
    return int(inp())

def linp(): 
    return list(map(int, inp().split()))


def solve():
    # Read input
    

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