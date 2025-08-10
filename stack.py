
# Implements a simple LIFO stack with push and pop operations

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
