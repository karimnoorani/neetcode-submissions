class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = UnionFind(len(accounts))
        indexMap = defaultdict(list)

        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                indexMap[email].append(i)
        
        for email in indexMap:
            for index in indexMap[email][1:]:
                UF.union(indexMap[email][0], index)
        
        indexToEmails = defaultdict(set)
        for index in range(len(accounts)):
            parent = UF.find(index)
            for email in accounts[index][1:]:
                indexToEmails[parent].add(email)
        
        res = []
        for parent in indexToEmails:
            res.append([accounts[parent][0]] + sorted(list(indexToEmails[parent])))
        
        return res