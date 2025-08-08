"""
Interpolation Search Algorithm
------------------------------
Works on sorted lists with uniformly distributed values.
Uses the value of the target to guess the search position.
Time Complexity: O(log log n) for uniform data, O(n) worst-case.
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    low, high = 0, len(data) - 1
    while low <= high and target >= data[low] and target <= data[high]:
        if low == high:
            return low if data[low] == target else -1

        pos = low + ((high - low) * (target - data[low]) // (data[high] - data[low]))
        if data[pos] == target:
            return pos
        elif data[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60]
    target = 50
    print(f"Target found at index: {search(data, target)}")
