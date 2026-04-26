class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = set([(0, 0)])
        for d in path:
            if d == 'N' or d == 'S':
                y += -1 if d == 'N' else 1
            else:
                x += 1 if d == 'E' else -1
            
            if (x, y) in visited:
                return True
            
            visited.add((x, y))
        
        return False