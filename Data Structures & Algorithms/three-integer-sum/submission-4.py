class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        
        while i < len(nums)-2:
            l, r = i+1, len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        
        return res