class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, height * (i-index))
            stack.append([start, h])
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights)-i))
        
        return maxArea