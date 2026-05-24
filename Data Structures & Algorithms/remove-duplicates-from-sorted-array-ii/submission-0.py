class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        nums.append(10001)
        for right in range(1, len(nums)-1):
            if nums[right] != nums[right-1] or nums[right] != nums[right+1]:
                nums[left] = nums[right]
                left += 1
        
        return left