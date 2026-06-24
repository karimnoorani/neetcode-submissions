class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        element = nums[0]

        for num in nums:
            count += 1 if num == element else -1
            if count == 0:
                element = num
                count = 1
        
        return element