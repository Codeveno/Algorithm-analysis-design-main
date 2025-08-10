# Implements a double-ended queue with add/remove from front/rear

from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        self.items.appendleft(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.items.popleft()

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    d = Deque()
    d.add_rear(10)
    d.add_front(20)
    print(d.remove_front())
    print(d.remove_rear())
