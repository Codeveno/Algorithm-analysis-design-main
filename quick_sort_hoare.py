def hoare_partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, p)
        quick_sort_hoare(arr, p + 1, high)

if __name__ == "__main__":
    data = [8, 4, 7, 3, 10, 5]
    quick_sort_hoare(data)
    print("Sorted array:", data)
