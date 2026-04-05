class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] >= stack[-1]:
                stack.pop()
                res[i] += 1
            res[i] += 1 if stack else 0
            stack.append(heights[i])
        
        return res