class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, n):
        while self.par[n] != n:
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

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        UF = UnionFind(len(nums))
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if UF.find(i) == UF.find(j):
                    continue
                
                if math.gcd(nums[i], nums[j]) > 1:
                    UF.union(i, j)
        
        return UF.count == 1