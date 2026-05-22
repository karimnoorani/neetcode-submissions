class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def getTransformedNum(num):
            return a*(num*num)+b*num+c
        
        left, right = 0, len(nums)-1
        res = []

        while left <= right:
            if a > 0:
                if getTransformedNum(nums[left]) > getTransformedNum(nums[right]):
                    res.append(getTransformedNum(nums[left]))
                    left += 1
                else:
                    res.append(getTransformedNum(nums[right]))
                    right -= 1
            else:
                if getTransformedNum(nums[left]) < getTransformedNum(nums[right]):
                    res.append(getTransformedNum(nums[left]))
                    left += 1
                else:
                    res.append(getTransformedNum(nums[right]))
                    right -= 1
        
        return res[::-1] if a > 0 else res