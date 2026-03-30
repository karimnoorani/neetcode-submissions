class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        adjRow = {i:[] for i in range(1, k+1)}
        adjCol = {i:[] for i in range(1, k+1)}
        for u, v in rowConditions:
            adjRow[v].append(u)
        
        for u, v in colConditions:
            adjCol[v].append(u)
        
        visitingRow = set()
        visitedRow = set()

        visitingCol = set()
        visitedCol = set()

        res = []
        def dfs(n, visiting, visited, adj):
            if n in visiting:
                return False
            
            if n in visited:
                return True
            
            visiting.add(n)
            for nei in adj[n]:
                if not dfs(nei, visiting, visited, adj):
                    return False
            visiting.remove(n)
            visited.add(n)
            res.append(n)
            return True
        
        for i in range(1, k+1):
            if not dfs(i, visitingRow, visitedRow, adjRow):
                return []
        
        rowTop = res[:]
        res = []
        for i in range(1, k+1):
            if not dfs(i, visitingCol, visitedCol, adjCol):
                return []
        colTop = res[:]

        matrix = [[0 for _ in range(k)] for _ in range(k)]
        
        for i in range(1, k+1):
            matrix[rowTop.index(i)][colTop.index(i)] = i
        
        return matrix