#!/usr/bin/env python3
import sys
from typing import List

# File I/O setup
sys.stdin = open('in4.txt', 'r')
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

def validCorner(r, c, row_start, col_start) -> bool:
    # Check diagonals for X pattern
    return ((r == row_start and (c == col_start + 1 - 1 or c == col_start + 1 + 1)) or 
            (r == row_start + 2 and (c == col_start + 1 - 1 or c == col_start + 1 + 1)))

def isValid(r, c, ROWS, COLS):
    return 0 <= r < ROWS and 0 <= c < COLS

def validSubGrid(row, col, ROWS, COLS, matrix, verifier) -> bool:
    if col == 0 or col >= COLS - 2:  # Need space for the X pattern
        return False
        
    sub_tuple = []
    for r in range(row, row + 3):
        row_tuple = []
        for c in range(col, col + 3):
            if isValid(r, c, ROWS, COLS):
                if validCorner(r, c, row, col):
                    row_tuple.append(matrix[r][c])
                elif r == row + 1 and c == col + 1:  # Center A
                    row_tuple.append(matrix[r][c])
                else:
                    row_tuple.append('.')
        sub_tuple.append(tuple(row_tuple))
    
    sub_tuple = tuple(sub_tuple)
    return sub_tuple in verifier
                
def solve():
    # Read the grid into a matrix
    matrix = read_matrix()
    
    # Define valid X-MAS patterns (M.S, .A., M.S) and its variations
    v1 = (('M', '.', 'S'), ('.', 'A', '.'), ('M', '.', 'S'))  # MAS/MAS
    v2 = (('S', '.', 'M'), ('.', 'A', '.'), ('S', '.', 'M'))  # SAM/SAM
    v3 = (('M', '.', 'S'), ('.', 'A', '.'), ('S', '.', 'M'))  # MAS/SAM
    v4 = (('S', '.', 'M'), ('.', 'A', '.'), ('M', '.', 'S'))  # SAM/MAS
    
    verifier = {v1, v2, v3, v4}
    
    ans = 0
    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(ROWS - 2):
        for c in range(COLS - 2):
            if validSubGrid(r, c, ROWS, COLS, matrix, verifier):
                ans += 1
    
    print(ans)
    return ans

def main():
    # For single test case
    solve()
    
if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()
        