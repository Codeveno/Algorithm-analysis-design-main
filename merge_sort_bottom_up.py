def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def merge_sort_bottom_up(arr):
    n = len(arr)
    width = 1
    result = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i:i+width]
            right = result[i+width:i+2*width]
            result[i:i+2*width] = merge(left, right)
        width *= 2
    return result

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted array:", merge_sort_bottom_up(data))
