def counting_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    for number in arr:
        count[number - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for number in reversed(arr):
        output[count[number - min_val] - 1] = number
        count[number - min_val] -= 1
    return output

if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Sorted array:", counting_sort(data))
