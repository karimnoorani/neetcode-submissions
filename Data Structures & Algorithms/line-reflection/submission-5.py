class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points.sort()
        n = len(points)
        
        min_point = points[0]
        max_point = points[n-1]
        line = (max_point[0] + min_point[0])/2

        new_points = set()
        for i in range(n):
            x, y = points[i]
            d = abs(x-line)
            new_points.add((line+d if x < line else line-d, y))
        
        return set([(x, y) for x, y in points]) == set(new_points)