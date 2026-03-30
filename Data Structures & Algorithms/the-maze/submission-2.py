class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])

        start = [start[0], start[1]]
        destination = [destination[0], destination[1]]

        visited = set()
        def dfs(r, c):
            if [r, c] == destination:
                return True
            
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r, c
                while 0 <= newR+dR < ROWS and 0 <= newC+dC < COLS and maze[newR+dR][newC+dC] != 1:
                    newR += dR
                    newC += dC
                if (newR, newC) not in visited and dfs(newR, newC):
                    return True
            return False
        
        return dfs(start[0], start[1])