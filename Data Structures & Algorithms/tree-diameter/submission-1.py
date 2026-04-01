class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0
        n = len(edges)+1
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visiting = set()

        def dfs(node):
            visiting.add(node)
            res = 0
            for nei in adjList[node]:
                if nei not in visiting:
                    res = max(res, 1+dfs(nei))
            visiting.remove(node)
            return res
        
        res = 1
        for i in range(n):
            res = max(res, dfs(i))
        
        return res