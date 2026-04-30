class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(cur, par):
            time = 0
            for nei in adjList[cur]:
                if nei == par:
                    continue
                neiTime = dfs(nei, cur)
                if neiTime or hasApple[nei]:
                    time += 2 + neiTime
            return time
        
        return dfs(0, None)