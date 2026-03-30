class UnionFind:
    def __init__(self, n: int) -> None:
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(a, b, w, i) for i, (a, b, w) in enumerate(edges)]
        edges.sort(key=lambda e: e[2])

        def findMST(include=None, exclude=None):
            uf = UnionFind(n)
            total = 0
            edgeCount = 0
            if include is not None:
                a, b, w, orig_i = edges[include]
                uf.union(a, b)
                total += w
                edgeCount += 1
            
            for i, e in enumerate(edges):
                if i == include or i == exclude:
                    continue
                a, b, w, orig_i = e
                if uf.union(a, b):
                    total += w
                    edgeCount += 1
            
            return total if edgeCount == n-1 else float('INF')
        
        mst_cost = findMST()
        critical = []
        p_critical = []
        
        for i, e in enumerate(edges):
            if findMST(exclude=i) > mst_cost:
                critical.append(e[3])
            else:
                if findMST(include=i) == mst_cost:
                    p_critical.append(e[3])
        
        return [critical, p_critical]