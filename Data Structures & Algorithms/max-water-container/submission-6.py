class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        res = 0

        while L < R:
            res = max(res, (R-L)*(min(heights[L], heights[R])))

            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1
        
        return res