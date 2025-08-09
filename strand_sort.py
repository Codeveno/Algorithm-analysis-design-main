def strand_sort(arr):
    if not arr:
        return []
    result = []
    while arr:
        sub = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] > sub[-1]:
                sub.append(arr.pop(i))
            else:
                i += 1
        # merge sub into result (both sorted)
        res = []
        i = j = 0
        while i < len(result) and j < len(sub):
            if result[i] <= sub[j]:
                res.append(result[i]); i += 1
            else:
                res.append(sub[j]); j += 1
        res.extend(result[i:]); res.extend(sub[j:])
        result = res
    return result

if __name__ == "__main__":
    data = [5, 1, 4, 2, 8, 0, 2]
    print("Sorted array:", strand_sort(data))
