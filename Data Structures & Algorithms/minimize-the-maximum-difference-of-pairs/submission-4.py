class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def isValid(maxDiff):
            index = 0
            totalPairs = 0

            while index < len(nums)-1:
                if nums[index+1]-nums[index] <= maxDiff:
                    totalPairs += 1
                    index += 2
                else:
                    index += 1
            
            return totalPairs >= p
        
        left, right = 0, nums[-1]-nums[0]
        minDiff = right
        while left <= right:
            middle = (left+right) // 2

            if isValid(middle):
                minDiff = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return minDiff
