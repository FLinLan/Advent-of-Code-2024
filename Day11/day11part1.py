#!/usr/bin/env python3
from collections import defaultdict
import sys
from typing import Dict, List

def read_input(filename: str = 'input2.txt') -> str:
    """Read and return the input file contents."""
    try:
        with open(filename, 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        sys.exit(1)

def step_stone(stone: str) -> List[str]:
    """Apply the transformation rules to a single stone.
    
    Rules:
    1. If stone is "0", becomes "1"
    2. If stone has even digits, splits into two stones
    3. Otherwise, multiply by 2024
    """
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        # Remove leading zeros from the right half
        right_half = str(int(stone[mid:]))
        return [stone[:mid], right_half]
    else:
        return [str(int(stone) * 2024)]

def simulate_blinks(stones: Dict[str, int], num_blinks: int) -> int:
    """Simulate the stone transformations for a specified number of blinks."""
    for _ in range(num_blinks):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for new_stone in step_stone(stone):
                new_stones[new_stone] += count
        stones = new_stones

    return sum(stones.values())

def solve(input_data: str, blinks: int = 75) -> int:
    """Solve the puzzle for the given number of blinks."""
    initial_stones = input_data.split()
    stones = {stone: 1 for stone in initial_stones}
    return simulate_blinks(stones, blinks)

def main():
    input_data = read_input()
    result = solve(input_data)
    print(result)

if __name__ == "__main__":
    main()
