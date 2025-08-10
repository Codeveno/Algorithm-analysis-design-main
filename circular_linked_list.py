# Implements a circular linked list with insert, delete, and traverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return
        curr = self.head
        prev = None
        while True:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if tail == self.head:
                        self.head = None
                        return
                    tail.next = curr.next
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    def traverse(self):
        if not self.head:
            print('List is empty')
            return
        curr = self.head
        while True:
            print(curr.data, end=' -> ')
            curr = curr.next
            if curr == self.head:
                break
        print('(back to head)')

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.traverse()
    cll.delete(1)
    cll.traverse()
