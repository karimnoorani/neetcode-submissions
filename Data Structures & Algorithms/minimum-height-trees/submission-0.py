
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def bfs(root):
            q = deque()
            visited = set()
            
            q.append(root)
            visited.add(root)
            
            height = 0
            while q:
                qLen = len(q)
                for _ in range(qLen):
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                if q:
                    height += 1
            return height
        
        stack = []
        heightMap = {}
        for node in range(n):
            heightMap[node] = bfs(node)
            while stack and heightMap[stack[-1]] > heightMap[node]:
                stack.pop()
            if stack and heightMap[stack[-1]] < heightMap[node]:
                continue
            stack.append(node)
        
        return stack
