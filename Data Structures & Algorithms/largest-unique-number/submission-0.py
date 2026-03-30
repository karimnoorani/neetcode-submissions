class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {n: 0 for n in set(nums)}
        for n in nums:
            freq[n] += 1
        
        maxNum = float('-inf')
        for n in set(nums):
            if freq[n] == 1:
                maxNum = max(maxNum, n)
        
        return maxNum if maxNum != float('-inf') else -1