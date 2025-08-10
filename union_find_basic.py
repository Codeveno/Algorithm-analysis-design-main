# Implements basic Union-Find (Disjoint Set) without optimizations

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0,1)
    print(uf.find(1))
