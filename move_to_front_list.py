# Implements a self-adjusting list that moves accessed items to front

class MoveToFrontList:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)

    def search(self, item):
        try:
            idx = self.data.index(item)
            self.data.insert(0, self.data.pop(idx))
            return True
        except ValueError:
            return False

    def delete(self, item):
        try:
            self.data.remove(item)
        except ValueError:
            pass

    def traverse(self):
        print(self.data)

if __name__ == "__main__":
    mtf = MoveToFrontList()
    mtf.insert(1)
    mtf.insert(2)
    mtf.search(2)
    mtf.traverse()
