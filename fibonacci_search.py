"""
Fibonacci Search Algorithm
--------------------------
Uses Fibonacci numbers to divide the list for searching.

Time Complexity: O(log n)
"""

def search(data, target):
    """
    Searches for the target in the data list.
    Returns the index if found, otherwise -1.
    """
    n = len(data)
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm1 + fibMMm2

    while fibM < n:
        fibMMm2, fibMMm1 = fibMMm1, fibM
        fibM = fibMMm1 + fibMMm2

    offset = -1
    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)
        if data[i] < target:
            fibM, fibMMm1, fibMMm2 = fibMMm1, fibMMm2, fibM - fibMMm1
            offset = i
        elif data[i] > target:
            fibM, fibMMm1, fibMMm2 = fibMMm2, fibMMm1 - fibMMm2, fibM - fibMMm1
        else:
            return i

    if fibMMm1 and offset + 1 < n and data[offset + 1] == target:
        return offset + 1
    return -1

if __name__ == "__main__":
    data = [10, 22, 35, 40, 45, 50, 80]
    target = 35
    print(f"Target found at index: {search(data, target)}")
    
