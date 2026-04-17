class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
        visiting = set()
        visited = set()
        
        if len(adjList[destination]) != 0:
            return False
        
        def dfs(node):
            if node in visited or node == destination:
                return True
            
            if node in visiting or len(adjList[node]) == 0:
                return False
            
            visiting.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        return dfs(source)
            