class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        frequency = {0: 0, 1: 0}
        maxZeros = 0
        left = 0

        for right in range(len(nums)):
            frequency[nums[right]] += 1

            while frequency[0] > k:
                frequency[nums[left]] -= 1
                left += 1
            
            maxZeros = max(maxZeros, right-left+1)
        
        return maxZeros
