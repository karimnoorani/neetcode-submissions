class Solution:
    def trap(self, height: List[int]) -> int:
        postfix = [0] * len(height)
        prefix = [0] * len(height)
        res = [0] * len(height)

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i+1])
        
        for i in range(len(height)):
            trappedWater = min(prefix[i], postfix[i]) - height[i]
            res[i] = trappedWater if trappedWater > 0 else 0
        print(prefix)
        print(postfix)
        print(res)
        return sum(res)
            