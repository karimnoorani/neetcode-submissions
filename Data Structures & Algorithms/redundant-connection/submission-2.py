class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {i:i for i in range(1, len(edges)+1)}
        rank = {i:0 for i in range(1, len(edges)+1)}

        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p1] += 1
            
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
