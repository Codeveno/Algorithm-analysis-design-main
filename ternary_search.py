"""
Ternary Search Algorithm
------------------------
Works on sorted lists. Divides the list into three parts instead of two.
Time Complexity: O(log₃ n)
Space Complexity: O(1)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2

        if target < data[mid1]:
            right = mid1 - 1
        elif target > data[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    target = 6
    print(f"Target found at index: {search(data, target)}")
