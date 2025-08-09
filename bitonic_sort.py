def bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if (direction == 1 and arr[i] > arr[i + k]) or (direction == 0 and arr[i] < arr[i + k]):
                arr[i], arr[i + k] = arr[i + k], arr[i]
        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, k, direction)

def bitonic_sort_rec(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_rec(arr, low, k, 1)
        bitonic_sort_rec(arr, low + k, k, 0)
        bitonic_merge(arr, low, cnt, direction)

def bitonic_sort(arr):
    # bitonic sort requires size to be power of two; pad if necessary
    n = len(arr)
    pow2 = 1
    while pow2 < n:
        pow2 <<= 1
    padded = arr[:] + [max(arr) + 1] * (pow2 - n) if arr else []
    bitonic_sort_rec(padded, 0, len(padded), 1)
    return padded[:n]

if __name__ == "__main__":
    data = [3, 7, 4, 8, 6, 2, 1, 5]
    print("Sorted array:", bitonic_sort(data))
