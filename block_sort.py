# Block sort (simple block merge approach): divide array into blocks of size B = sqrt(n),
# sort each block, then merge blocks using an auxiliary list.
import math
def block_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    B = int(math.sqrt(n)) or 1
    # sort each block
    for i in range(0, n, B):
        arr[i:i+B] = sorted(arr[i:i+B])
    # simple k-way merge of sorted blocks
    import heapq
    heap = []
    blocks = []
    for i in range(0, n, B):
        blocks.append((i, min(i+B, n)))
    for idx, (start, end) in enumerate(blocks):
        if start < end:
            heapq.heappush(heap, (arr[start], idx, start))
    res = []
    while heap:
        val, bidx, pos = heapq.heappop(heap)
        res.append(val)
        start, end = blocks[bidx]
        pos += 1
        if pos < end:
            heapq.heappush(heap, (arr[pos], bidx, pos))
    return res

if __name__ == "__main__":
    data = [9, 1, 8, 3, 7, 4, 6, 2, 5, 0]
    print("Sorted array:", block_sort(data))
