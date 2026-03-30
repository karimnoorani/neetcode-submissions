class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        
        for x2, y2 in self.points:
            if x1 == x2 or y1 == y2:
                continue

            if abs(x1-x2) == abs(y1-y2):
                res += self.points.get(tuple([x1, y2]), 0) * self.points.get(tuple([x2, y1]), 0) * self.points.get(tuple([x2, y2]), 0)
        
        return res