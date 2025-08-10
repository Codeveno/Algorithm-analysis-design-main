# Implements a doubly linked list with insert, delete and traverse

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if not curr:
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=' <-> ')
            curr = curr.next
        print('None')

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.traverse_forward()
    dll.delete(1)
    dll.traverse_forward()
