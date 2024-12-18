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

def setupFile(disk_map):
    file = []
    id = 0
    N = len(disk_map)
    for i in range(N):
        if i % 2 == 0:
            pushSpace(file, id, 0, disk_map[i])
            id += 1
        else:
            pushSpace(file, id, 1, disk_map[i])
    return file

def solve():
    # Reading input string
    disk_map = inp()
    # Output the input string to verify
    # alternate between the
    file = setupFile(disk_map)

    R = len(file) - 1

    block_id = 9 # moving each blocks with the same ID
    block_size, gap_size = 0, 0
    for L in range(len(file)):
        if L > R: break
        if L <= R and file[L] == '.' and file[R] != '.' and file[R] == block_id:
            L += 1
            R -= 1
            block_size += 1
            gap_size += 1
            if block_size == gap_size:
                moveBlock()
        # while R >= 0 and file[R] == '.':
        #     R -= 1
    # we know that file ID is sorted in an ascending order (given my prompt),
    # starting from the very left, pick the blocks, if they can fit in the gaps, replace them
    # if not, continue with the next block instead

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
