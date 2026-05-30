class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            prev_index = index
            while stack and height <= stack[-1][0]:
                prev_height, prev_index = stack.pop()
                maxArea = max(maxArea, prev_height*(index-prev_index))
                print(maxArea)
            stack.append([height, prev_index])
        
        return maxArea