class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        for i in range(len(maze)):
            maze[i] = [1] + maze[i] + [1]
        ROWS, COLS = len(maze), len(maze[0])
        maze.insert(0, [1 for _ in range(COLS)])
        maze.append([1 for _ in range(COLS)])

        start = [start[0]+1, start[1]+1]
        destination = [destination[0]+1, destination[1]+1]

        visited = set()
        def dfs(r, c):
            if [r, c] == destination:
                return True
            
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r, c
                while maze[newR+dR][newC+dC] != 1:
                    newR += dR
                    newC += dC
                if (newR, newC) not in visited and dfs(newR, newC):
                    return True
            visited.remove((r, c))
            return False
        
        return dfs(start[0], start[1])