class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = set()
        UF = UnionFind(n)
        
        for a, b in edges:
            UF.union(a, b)
        
        for i in range(n):
            components.add(UF.find(i))
        
        return len(components)

