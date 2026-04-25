class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        prefix = [float('-inf')]
        for i in range(1, len(nums)):
            prefix.append(max(prefix[i-1], nums[i-1]))
        
        postfix = [float('inf') for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = min(postfix[i+1], nums[i+1])
        
        res = 0
        for i in range(len(nums)):
            if nums[i] >= prefix[i] and nums[i] <= postfix[i]:
                res += 1
        
        return res