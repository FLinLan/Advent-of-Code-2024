#!/usr/bin/env python3
import sys
from typing import List

# File I/O setup
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def isIncreasing(nums: List[int]) -> bool:
    """Check if the list is strictly increasing."""
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            return False
    return True

def isDecreasing(nums: List[int]) -> bool:
    """Check if the list is strictly decreasing."""
    for i in range(1, len(nums)):
        if nums[i-1] <= nums[i]:
            return False
    return True

def inBounds(nums: List[int]) -> bool:
    """Check if the list meets the bounds criteria."""
    if not (isIncreasing(nums) or isDecreasing(nums)):
        return False
    
    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i-1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def isSafeWithDampener(nums: List[int]) -> bool:
    """Check if the list is safe or can be made safe by removing one level."""
    if inBounds(nums):
        return True
    
    # Try removing each level and check
    for i in range(len(nums)):
        modified = nums[:i] + nums[i+1:]  # Remove the i-th element
        if inBounds(modified):
            return True
    
    return False

def solve():
    safe_count = 0
    for line in sys.stdin:
        if line.strip():  # Ignore empty lines
            nums = list(map(int, line.split()))
            if isSafeWithDampener(nums):
                safe_count += 1
    
    print(safe_count)

def main():
    solve()

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    try:
        main()
    finally:
        sys.stdin.close()
        sys.stdout.close()
        