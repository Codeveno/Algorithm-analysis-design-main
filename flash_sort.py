# Flash sort: approximate linear-time distribution-based sort for many distributions.
def flash_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr[:]
    m = int(0.43 * n) or 1
    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
        return arr[:]
    # class counts
    L = [0] * m
    c1 = (m - 1) / (max_val - min_val)
    for x in arr:
        k = int(c1 * (x - min_val))
        L[k] += 1
    for i in range(1, m):
        L[i] += L[i - 1]
    # permute
    arr_copy = arr[:]
    i = 0
    nmove = 0
    j = 0
    while nmove < n:
        while j >= L[int(c1 * (arr_copy[i] - min_val))]:
            i += 1
        k = int(c1 * (arr_copy[i] - min_val))
        while j < L[k]:
            k = int(c1 * (arr_copy[i] - min_val))
            dest = L[k] - 1
            arr_copy[dest], arr_copy[i] = arr_copy[i], arr_copy[dest]
            L[k] -= 1
            nmove += 1
        j += 1
    # final insertion sort
    for i in range(1, n):
        key = arr_copy[i]; j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]; j -= 1
        arr_copy[j + 1] = key
    return arr_copy

if __name__ == "__main__":
    data = [4, 1, 3, 2, 8, 5, 6, 7]
    print("Sorted array:", flash_sort(data))
