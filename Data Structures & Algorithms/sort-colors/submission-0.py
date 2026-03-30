class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0] * 3
        for num in nums:
            buckets[num] += 1
        
        cur = 0
        for i in range(len(buckets)):
            for j in range(buckets[i]):
                nums[cur] = i
                cur += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        