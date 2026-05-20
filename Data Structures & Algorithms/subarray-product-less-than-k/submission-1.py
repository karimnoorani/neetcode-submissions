class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        totalSubarrays = 0
        product = 1
        left = 0
        
        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            
            totalSubarrays += right-left+1
        
        return totalSubarrays