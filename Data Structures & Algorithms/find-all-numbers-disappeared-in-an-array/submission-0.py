class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        while i < len(nums):
            n = nums[i]
            if nums[n-1] != n:
                nums[i], nums[n-1] = nums[n-1], nums[i]
            else:
                i += 1
                
        for i, n in enumerate(nums):
            if n != i+1:
                res.append(i+1)
        
        return res