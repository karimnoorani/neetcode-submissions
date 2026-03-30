class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = set()

        for num in nums:
            if num in numsMap:
                return True
            else:
                numsMap.add(num)
        
        return False
         