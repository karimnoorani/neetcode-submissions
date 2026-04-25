class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)

        arr1 = []
        for n in nums1:
            if n not in nums2:
                arr1.append(n)
        
        arr2 = []
        for n in nums2:
            if n not in nums1:
                arr2.append(n)
        
        return [arr1, arr2]