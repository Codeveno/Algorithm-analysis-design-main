def three_way_quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low >= high:
        return
    lt = low
    gt = high
    pivot = arr[low]
    i = low
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1; i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    three_way_quick_sort(arr, low, lt - 1)
    three_way_quick_sort(arr, gt + 1, high)

if __name__ == "__main__":
    data = [2, 3, 2, 1, 2, 3, 1]
    three_way_quick_sort(data)
    print("Sorted array:", data)
