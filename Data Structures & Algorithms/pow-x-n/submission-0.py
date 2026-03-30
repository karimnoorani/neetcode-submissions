class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        while n != 0:
            if n > 0:
                res *= x
                n -= 1
            else:
                res = res/x
                n += 1 
        return res