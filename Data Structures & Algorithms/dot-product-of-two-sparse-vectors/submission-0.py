class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nums[i] = n
        self.maxIndex = len(nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(max(self.maxIndex, vec.maxIndex)):
            res += self.nums.get(i, 0) * vec.nums.get(i, 0)
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
