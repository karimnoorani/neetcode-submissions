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
            return False
        
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        
        self.count -= 1
        return True if self.count == 1 else False

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        heapq.heapify(logs)
        UF = UnionFind(n)

        while logs:
            timestamp, x, y = heapq.heappop(logs)

            if UF.union(x, y):
                return timestamp
        
        return -1