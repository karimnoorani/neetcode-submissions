class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        elementsToRemove = []
        for num in nums:
            if num in seen:
                elementsToRemove.append(num)
            else:
                seen.add(num)
        
        for item in elementsToRemove:
            nums.remove(item)
        
        return len(nums)