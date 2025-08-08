"""
Jump Search Algorithm
---------------------
Works on sorted lists. Jumps ahead by fixed steps, then does a linear search in the block.
Time Complexity: O(√n)
Space Complexity: O(1)
"""

import math

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    length = len(data)
    step = int(math.sqrt(length))
    prev = 0

    while prev < length and data[min(step, length) - 1] < target:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1

    while prev < min(step, length):
        if data[prev] == target:
            return prev
        prev += 1
    return -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    target = 11
    print(f"Target found at index: {search(data, target)}")
