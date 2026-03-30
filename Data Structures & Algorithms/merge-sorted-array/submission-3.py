class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mergedNums = []
        p1, p2 = 0, 0
        
        while p1 < m or p2 < n:
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    mergedNums.append(nums1[p1])
                    p1 += 1
                else:
                    mergedNums.append(nums2[p2])
                    p2 += 1
            elif p1 < m:
                mergedNums.append(nums1[p1])
                p1 += 1
            else:
                mergedNums.append(nums2[p2])
                p2 += 1
        
        for i in range(len(mergedNums)):
            nums1[i] = mergedNums[i]
        """
        Do not return anything, modify nums1 in-place instead.
        """
        