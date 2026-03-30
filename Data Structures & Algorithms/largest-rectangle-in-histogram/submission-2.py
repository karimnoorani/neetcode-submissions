class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][0]:
                popH, popI = stack.pop()
                maxArea = max(maxArea, popH*(i-popI))
                index = popI
            stack.append([h, index])
            print(stack, maxArea)
        
        return maxArea