class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums2 if A == nums1 else nums1
        total = len(nums1) + len(nums2)
        half = total // 2
        
        L, R = 0, len(A)-1
        while True:
            i = (L+R) // 2
            j = half-i-2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                R = i - 1
            else:
                L = i + 1
