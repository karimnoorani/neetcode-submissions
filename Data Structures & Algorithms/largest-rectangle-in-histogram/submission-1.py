class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)+1):
            h1 = heights[i] if i < len(heights) else -1
            k = i
            while stack and stack[-1][1] > h1:
                j, h2 = stack.pop()
                res = max(res, (i-j)*h2)
                k = j
            stack.append([k, h1])
        
        return res
            