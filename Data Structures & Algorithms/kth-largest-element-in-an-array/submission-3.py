class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if k > p: return quickSelect(p+1, r)
            elif k < p: return quickSelect(l, p-1)
            return nums[p]
        
        return quickSelect(0, len(nums)-1)
