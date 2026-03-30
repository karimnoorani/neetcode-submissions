from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)
        def strSort(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(strSort))
        return str(int("".join(nums)))