class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0
        n = len(edges)+1
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        leaves = []
        
        for node in adjList:
            if len(adjList[node]) == 1:
                leaves.append(node)
        
        layers = 0
        vertex_count = n
        while vertex_count > 2:
            vertex_count -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                nei = adjList[leaf].pop()
                adjList[nei].remove(leaf)
                if len(adjList[nei]) == 1:
                    next_leaves.append(nei)
            layers += 1
            leaves = next_leaves
        
        return layers * 2 + (0 if vertex_count == 1 else 1)