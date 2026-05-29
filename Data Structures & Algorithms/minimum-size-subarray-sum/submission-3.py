class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subarray_sum = 0
        res = float('inf')

        for right in range(len(nums)):
            subarray_sum += nums[right]

            while subarray_sum >= target:
                res = min(res, right-left+1)
                subarray_sum -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0