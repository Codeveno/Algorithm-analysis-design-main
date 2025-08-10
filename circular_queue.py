# Implements a fixed-size circular queue with enqueue and dequeue

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    print(cq.dequeue())
