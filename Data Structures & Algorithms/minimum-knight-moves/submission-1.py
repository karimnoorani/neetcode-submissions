class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([[0, 0, 0]]) # X, Y, STEPS
        visited = set([(0, 0)])

        while q:
            xi, yi, steps = q.popleft()

            if xi == x and yi == y:
                return steps
            
            for dX, dY in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                newX, newY = xi+dX, yi+dY
                if (newX, newY) not in visited:
                    q.append([newX, newY, steps+1])
                    visited.add((newX, newY))