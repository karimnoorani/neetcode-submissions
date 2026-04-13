class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 1
        res = [0 for _ in range(len(nums))]
        for n in nums:
            if n > 0:
                res[pos] = n
                pos += 2
            else:
                res[neg] = n
                neg += 2
        return res
            