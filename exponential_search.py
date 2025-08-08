"""
Exponential Search Algorithm
----------------------------
Finds the range where the element could be, then applies binary search.
Time Complexity: O(log n)
"""

def binary_search(data, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    if data[0] == target:
        return 0
    index = 1
    while index < len(data) and data[index] <= target:
        index *= 2
    return binary_search(data, target, index // 2, min(index, len(data) - 1))

if __name__ == "__main__":
    data = [2, 4, 6, 8, 10, 12, 14]
    target = 10
    print(f"Target found at index: {search(data, target)}")
