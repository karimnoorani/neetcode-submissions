class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1Length = len(nums1)-len(nums2)
        for i in range(nums1Length, len(nums1)):
            nums1[i] = nums2[i-nums1Length]
            j = i-1
            while j >= 0 and nums1[j+1] < nums1[j]:
                tmp = nums1[j]
                nums1[j] = nums1[j+1]
                nums1[j+1] = tmp
                j -= 1


        """
        Do not return anything, modify nums1 in-place instead.
        """
        