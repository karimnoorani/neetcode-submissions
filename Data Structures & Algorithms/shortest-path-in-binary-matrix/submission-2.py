class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque([(0, 0)])
        length = 1
        visited = set([(0, 0)])
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                if r == n-1 and c == n-1:
                    return length
                
                visited.add((r, c))
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    newR, newC = r+dR, c+dC
                    if min(newR, newC) < 0 or max(newR, newC) >= n or grid[newR][newC] == 1 or (newR, newC) in visited:
                        continue
                    q.append((newR, newC))
                    visited.add((newR, newC))
            length += 1
        
        return -1