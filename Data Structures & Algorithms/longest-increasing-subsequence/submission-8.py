import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        for i in range(1, len(nums)):
            print(tails)
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                index = bisect.bisect_left(tails, nums[i])
                tails[index] = nums[i]
        
        return len(tails)