class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        k = 0
        for num in nums.copy():
            if num in numSet:
                print(num)
                nums.remove(num)
                k += 1
            else:
                numSet.add(num)
        return len(nums)