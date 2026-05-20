class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.provinces = n
    
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
        
        self.provinces -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        UF = UnionFind(n)

        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col]:
                    UF.union(row, col)
        
        return UF.provinces