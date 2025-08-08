"""
Binary Search Algorithm
-----------------------
Works on sorted lists. Repeatedly divides the search interval in half.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    data = [2, 3, 4, 5, 8]
    target = 4
    print(f"Target found at index: {search(data, target)}")
