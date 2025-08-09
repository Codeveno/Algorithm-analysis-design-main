def msd_radix_sort(arr):
    if len(arr) <= 1:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp >= 10:
        exp *= 10

    def bucket_sort_by_digit(a, exp):
        if len(a) <= 1 or exp == 0:
            return a
        buckets = [[] for _ in range(10)]
        for num in a:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        res = []
        for b in buckets:
            if b:
                res.extend(bucket_sort_by_digit(b, exp // 10))
        return res

    return bucket_sort_by_digit(arr, exp)

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Sorted array:", msd_radix_sort(data))
