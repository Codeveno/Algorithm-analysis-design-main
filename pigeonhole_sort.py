def pigeonhole_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    holes = [0] * size
    for x in arr:
        holes[x - min_val] += 1
    res = []
    for i in range(size):
        res.extend([i + min_val] * holes[i])
    return res

if __name__ == "__main__":
    data = [8, 3, 2, 7, 4, 6, 8]
    print("Sorted array:", pigeonhole_sort(data))
