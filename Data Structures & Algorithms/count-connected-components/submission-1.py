class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            print(node)
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            if rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
        
        for n1, n2 in edges:
            union(n1, n2)
        
        for i in range(n):
            find(i)
        
        return len(set(par))