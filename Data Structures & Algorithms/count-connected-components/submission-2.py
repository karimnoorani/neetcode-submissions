class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adjList[node]:
                dfs(n)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res