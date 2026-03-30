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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = UnionFind(len(accounts))
        emailToIndex = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToIndex:
                    UF.union(emailToIndex[e], i)
                else:
                    emailToIndex[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToIndex.items():
            leader = UF.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + e)
        
        return res