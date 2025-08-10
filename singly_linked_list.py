# Implements a singly linked list with insert, delete, and traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def delete(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            return
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print('None')

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.traverse()
    sll.delete(1)
    sll.traverse()
