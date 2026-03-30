class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums.copy():
            if num == val:
                nums.remove(val)
        return len(nums)