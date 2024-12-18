#!/usr/bin/env python3
import sys
from typing import Dict

# File I/O setup
sys.stdin = open('input2.txt', 'r')

def inp():
    return sys.stdin.readline().strip()

def pushSpace(file, id, parity, times):
    for _ in range(int(times)):
        if parity == 0:
            file.append(id)
        else:
            file.append('.')

def solve():
    # Reading input string
    disk_map = inp()
    # Output the input string to verify
    # alternate between the
    id = 0
    file = []
    N = len(disk_map)
    for i in range(N):
        if i % 2 == 0:
            pushSpace(file, id, 0, disk_map[i])
            id += 1
        else:
            pushSpace(file, id, 1, disk_map[i])

    R = len(file) - 1
    for L in range(len(file)):
        if L > R: break
        if file[L] == '.' and file[R] != '.':
            file[L], file[R] = file[R], file[L]
        while R >= 0 and file[R] == '.':
            R -= 1

    ans = 0
    for i, n in enumerate(file):
        if n != '.':
            ans += (i * n)
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