class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == N or c == N or (r, c) in visited or grid[r][c] == 0:
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                neiR, neiC = r+dr, c+dc
                dfs(neiR, neiC)
        
        def BFS():
            res, q = 0, deque(visited)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    visited.add((r, c))
                    for dr, dc in directions:
                        neiR, neiC = r+dr, c+dc
                        if min(neiR, neiC) < 0 or neiR == N or neiC == N or (neiR, neiC) in visited:
                            continue
                        
                        if grid[neiR][neiC] == 1:
                            return res
                        
                        visited.add((neiR, neiC))
                        q.append([neiR, neiC])
                res += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return BFS()