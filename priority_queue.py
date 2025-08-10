# Implements a min-priority queue using heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty priority queue")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(2, 'code')
    pq.push(1, 'write')
    print(pq.pop())
