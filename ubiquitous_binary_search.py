"""
Ubiquitous Binary Search
------------------------
A variation of binary search used to find first/last occurrences in sorted arrays.
Time Complexity: O(log n)
"""

def search(data, target):
    """
    Searches for the first occurrence of the target in the data list.
    Returns the index if found, otherwise -1.
    """
    left, right = 0, len(data) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            result = mid
            right = mid - 1  
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    data = [1, 2, 4, 4, 4, 5, 6]
    target = 4
    print(f"First occurrence index: {search(data, target)}")
