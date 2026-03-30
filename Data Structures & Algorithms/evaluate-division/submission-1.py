class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for eq, val in zip(equations, values):
            Ai, Bi = eq
            adjList[Bi].append([1/val, Ai])
            adjList[Ai].append([val, Bi])
        
        visiting = set()
        def dfs(src, dst):
            if src == dst:
                return 1
            
            visiting.add(src)
            res = -1
            for w, nei in adjList[src]:
                if nei in visiting:
                    continue
                prod = w*dfs(nei, dst)
                if prod > 0:
                    res = prod
                    break
            visiting.remove(src)
            return res
        
        res = []
        for Cj, Dj in queries:
            res.append(dfs(Cj, Dj) if Cj in adjList and Dj in adjList else -1)
        
        return res