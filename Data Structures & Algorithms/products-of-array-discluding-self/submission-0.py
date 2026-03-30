class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        for num in nums:
            res.append(total)
            total = total * num
        
        total = 1
        i = len(nums)-1
        for num in nums[::-1]:
            res[i] = res[i]*total
            total = total * num
            i -= 1
        
        return res