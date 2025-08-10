# Implements a skip list supporting insert, search, and delete

import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1)

class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.level = 0
        self.header = Node(None, self.MAX_LEVEL)

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None]*(self.MAX_LEVEL+1)
        curr = self.header
        for i in reversed(range(self.level+1)):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if not curr or curr.key != key:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level+1, lvl+1):
                    update[i] = self.header
                self.level = lvl
            new_node = Node(key, lvl)
            for i in range(lvl+1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        curr = self.header
        for i in reversed(range(self.level+1)):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.key == key

    def delete(self, key):
        update = [None]*(self.MAX_LEVEL+1)
        curr = self.header
        for i in reversed(range(self.level+1)):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr and curr.key == key:
            for i in range(self.level+1):
                if update[i].forward[i] != curr:
                    break
                update[i].forward[i] = curr.forward[i]
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

if __name__ == "__main__":
    sl = SkipList()
    sl.insert(3)
    sl.insert(6)
    print(sl.search(3))  # True
    sl.delete(3)
    print(sl.search(3))  # False
