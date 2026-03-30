class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == m or c == n or (r, c) in visited:
                return
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = r+dR, c+dC
                if min(neiR, neiC) < 0 or neiR == m or neiC == n or (neiR, neiC) in visited or grid[neiR][neiC] == 0:
                    continue
                dfs(neiR, neiC)
            
            return
        
        def getIslandCount():
            nonlocal visited
            visited = set()
            count = 0

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c)
                        count += 1
            
            return count
        
        res = []
        for r, c in positions:
            grid[r][c] = 1
            res.append(getIslandCount())
        
        return res