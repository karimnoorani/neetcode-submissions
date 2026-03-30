class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        L, R = 0, len(A)-1

        while True:
            M1 = (L+R) // 2
            M2 = half - M1 - 2

            Aleft = A[M1] if M1 >= 0 else float('-infinity')
            Aright = A[M1 + 1] if M1 + 1 < len(A) else float('infinity')
            Bleft = B[M2] if M2 >= 0 else float('-infinity')
            Bright = B[M2 + 1] if M2 + 1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                R = M1 - 1
            else:
                L = M1 + 1