class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points.sort()
        line_sum = (points[0][0]+points[-1][0])
        
        point_set = set([(x, y) for x, y in points])
        for x, y in points:
            if (line_sum - x, y) not in point_set:
                return False

        return True