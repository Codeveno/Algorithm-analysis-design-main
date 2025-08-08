"""
Sparse Table Search (Prefix Jump Search)
----------------------------------------
Used for searching in data structures with constant-time range queries.
Here simulated as skipping fixed powers of 2 steps.
Time Complexity: O(log n)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    n = len(data)
    step = 1 << (n.bit_length() - 1)
    index = 0
    while step:
        if index + step < n and data[index + step] <= target:
            index += step
        step >>= 1
    if data[index] == target:
        return index
    return -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    target = 7
    print(f"Target found at index: {search(data, target)}")
