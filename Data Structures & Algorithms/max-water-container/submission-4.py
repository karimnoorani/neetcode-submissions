class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxVol = 0

        while l < r:
            maxVol = max(maxVol, (r-l)*min(heights[r], heights[l]))

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return maxVol