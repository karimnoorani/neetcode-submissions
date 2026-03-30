class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1

        for p2 in range(1, len(nums)):
            if nums[p2] != nums[p2-1]:
                nums[p1] = nums[p2]
                p1 += 1
        
        return p1