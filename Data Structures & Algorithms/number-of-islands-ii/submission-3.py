class UnionFind:
    def __init__(self):
        self.par = {}
        self.size = {}
        self.islandCount = 0
    
    def addLand(self, r, c):
        if (r, c) in self.par:
            return
        self.par[(r, c)] = (r, c)
        self.size[(r, c)] = 1
        self.islandCount += 1

        for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neiR, neiC = r+dR, c+dC
            if (neiR, neiC) in self.par and self.union((r, c), (neiR, neiC)):
                self.islandCount -= 1
    
    def getIslandCount(self):
        return self.islandCount
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        UF = UnionFind()
        res = []
        
        for r, c in positions:
            UF.addLand(r, c)
            res.append(UF.getIslandCount())
        
        return res
