class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(1, len(edges)+1):
            adjList[i] = []
        
        for edge in edges:
            v1, v2 = edge
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        visited = set()
        cycleStart = -1

        def dfs(u, v):
            nonlocal cycleStart
            if u in visited:
                cycleStart = u
                return True
            
            visited.add(u)
            for neighbor in adjList[u]:
                if neighbor == v:
                    continue
                if dfs(neighbor, u):
                    return True
            
            visited.remove(u)
            return False
        
        for i in range(1, len(edges)+1):
            if dfs(i, -1):
                visited = set()
                dfs(cycleStart, -1)
        
        print(visited)
        for edge in edges[::-1]:
            v1, v2 = edge
            if v1 in visited and v2 in visited:
                return edge