def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort_lomuto(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = lomuto_partition(arr, low, high)
        quick_sort_lomuto(arr, low, p - 1)
        quick_sort_lomuto(arr, p + 1, high)

if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    quick_sort_lomuto(data)
    print("Sorted array:", data)
