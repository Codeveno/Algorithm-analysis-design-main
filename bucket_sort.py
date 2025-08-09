def bucket_sort(arr):
    if not arr:
        return arr
    # Works best for numbers in [0,1). Normalize for general cases
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr[:]
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = int((x - min_val) / (max_val - min_val) * (n - 1))
        buckets[idx].append(x)
    result = []
    for b in buckets:
        b.sort()  # using python sort for bucket internal sort
        result.extend(b)
    return result

if __name__ == "__main__":
    data = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Sorted array:", bucket_sort(data))
