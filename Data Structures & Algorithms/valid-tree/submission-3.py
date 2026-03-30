class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, n: int) -> int:
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = UnionFind(n)
        
        for n1, n2 in edges:
            if not UF.union(n1, n2):
                return False
        
        parents = set()
        for i in range(n):
            parents.add(UF.find(i))
        
        return len(parents) == 1