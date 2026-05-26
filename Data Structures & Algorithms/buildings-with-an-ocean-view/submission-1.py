class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()
            stack.append(index)
        return stack