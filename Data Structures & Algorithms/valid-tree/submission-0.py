class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        
        return True