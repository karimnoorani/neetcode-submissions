class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        
        postfix = [0 for _ in range(len(height))]
        for i in range(len(height)-2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i+1])

        total = 0
        for i in range(len(height)):
            total += max(0, min(prefix[i], postfix[i])-height[i])
        
        return total

