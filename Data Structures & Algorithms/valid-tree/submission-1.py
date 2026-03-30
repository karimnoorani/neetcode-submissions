class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adjList[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            
            return True
        
        if not dfs(0, n):
            return False
        
        return len(visited) == n