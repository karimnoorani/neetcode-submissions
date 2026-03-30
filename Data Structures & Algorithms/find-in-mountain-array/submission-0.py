class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        L, R = 0, mountainArr.length()-1

        while L <= R:
            M = (L+R)//2

            val = mountainArr.get(M)
            valLeft = mountainArr.get(M-1)
            valRight = mountainArr.get(M+1)

            if valLeft < val < valRight:
                L = M + 1
            elif valRight < val < valLeft:
                R = M - 1
            else:
                peak = M
                break
        
        res = -1
        L, R = 0, peak

        while L <= R and res == -1:
            M = (L+R)//2
            val = mountainArr.get(M)

            if val > target:
                R = M - 1
            elif val < target:
                L = M + 1
            else:
                res = M
        
        L, R = peak, mountainArr.length()-1
        while L <= R and res == -1:
            M = (L+R)//2
            val = mountainArr.get(M)

            if val > target:
                L = M + 1
            elif val < target:
                R = M - 1
            else:
                res = M
        
        return res


