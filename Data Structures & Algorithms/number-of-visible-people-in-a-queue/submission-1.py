class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = deque()
        result = [0 for _ in range(len(heights))]
        
        for index in range(len(heights)-1, -1, -1):
            canSee = 0
            while stack and heights[index] > stack[-1]:
                canSee += 1
                stack.pop()
            canSee += 1 if stack else 0
            result[index] = canSee
            stack.append(heights[index])
        
        return result