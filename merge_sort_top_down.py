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

def merge_sort_top_down(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_top_down(arr[:mid])
    right = merge_sort_top_down(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    sorted_data = merge_sort_top_down(data)
    print("Sorted array:", sorted_data)
