class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return
        
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        
        self.count -= 1
        return

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        UF = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    UF.union(i, j)
        
        return UF.count