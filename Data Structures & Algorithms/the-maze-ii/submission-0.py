class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        heap = [[0, start[0], start[1]]]
        visited = set()

        while heap:
            dist, r, c = heapq.heappop(heap)
            
            if [r, c] == destination:
                return dist
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r, c
                while 0 <= newR+dR < ROWS and 0 <= newC+dC < COLS and maze[newR+dR][newC+dC] != 1:
                    newR += dR
                    newC += dC
                if (newR, newC) not in visited:
                    heapq.heappush(heap, [dist+abs(r-newR)+abs(c-newC), newR, newC])
        
        return -1