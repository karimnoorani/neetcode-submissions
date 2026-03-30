
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        leaves = deque()
        edge_cnt = {}
        for node, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edge_cnt[node] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)