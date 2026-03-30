class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = 0
        res = []

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
            maxHeight = max(heights[i], maxHeight)
        
        return res[::-1]