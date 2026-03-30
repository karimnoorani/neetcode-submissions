class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        minSize = float('inf')
        while r < len(nums)+1:
            print(total, l, r)
            if total >= target:
                minSize = min(minSize, r-l)
                total -= nums[l]
                l += 1
            else:
                if r == len(nums):
                    break
                total += nums[r]
                r += 1
        
        return minSize if minSize < float('inf') else 0