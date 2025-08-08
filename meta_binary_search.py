"""
Meta Binary Search Algorithm
----------------------------
Uses the binary representation of the range to reduce comparisons.
Time Complexity: O(log n)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    n = len(data)
    lg = n.bit_length() - 1
    pos = 0
    for i in range(lg, -1, -1):
        if pos + (1 << i) < n and data[pos + (1 << i)] <= target:
            pos += 1 << i
    if data[pos] == target:
        return pos
    return -1

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    print(f"Target found at index: {search(data, target)}")
