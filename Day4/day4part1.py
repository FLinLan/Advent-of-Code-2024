#!/usr/bin/env python3
import sys
import math
from typing import List

# File I/O setup
sys.stdin = open('in3.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def inp(): 
    return sys.stdin.readline().strip()

def iinp(): 
    return int(inp())

def linp(): 
    return list(map(int, inp().split()))

def read_matrix() -> List[List[str]]:
    matrix = []
    while True:
        line = inp()
        if not line:
            break
        matrix.append(list(line))
    return matrix

def formWord(r, c, dr, dc, matrix):
    word = ""
    for i in range(4):
        nr, nc = r + dr * i, c + dc * i
        if not isValid(nr, nc, len(matrix), len(matrix[0])):
            return False
        word += matrix[nr][nc]
    return word == "XMAS" 
# or word == "SAMX"

def isValid(r, c, ROWS, COLS) -> bool:
    return 0 <= r < ROWS and 0 <= c < COLS

def countWords(r, c, ROWS, COLS, matrix):
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),       # Horizontal and Vertical
        (-1, 1), (1, -1), (-1, -1), (1, 1)      # Diagonals
    ]
    
    cnt = 0
    for dr, dc in directions:
        if formWord(r, c, dr, dc, matrix):
            cnt += 1
            
    return cnt
    
def solve():
    # Read the grid into a matrix
    matrix = read_matrix()
    
    ans = 0
    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] != '.':
                ans += countWords(r, c, ROWS, COLS, matrix)

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
        