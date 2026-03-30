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
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        edge_cnt = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1 and uf.union(i, j):
                    edge_cnt += 1
        
        return edge_cnt == len(nums)-1