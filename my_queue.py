# Implements a FIFO queue with enqueue and dequeue operations

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    print(q.dequeue())
