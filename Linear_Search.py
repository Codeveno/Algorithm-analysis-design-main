"""
Linear Search Algorithm
-----------------------
Goes through the list element-by-element from start to end until it finds the target.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    target = 4
    print(f"Target found at index: {search(data, target)}")
