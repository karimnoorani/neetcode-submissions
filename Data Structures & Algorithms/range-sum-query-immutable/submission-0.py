class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0 for _ in range(len(nums))]
        self.nums = nums
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i-1]+nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right]+self.prefix[right]-self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)