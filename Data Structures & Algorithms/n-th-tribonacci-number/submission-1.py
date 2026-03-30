class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1

        n_3 = 0
        n_2 = 1
        n_1 = 1

        for i in range(n-2):
            n_3, n_2, n_1 = n_2, n_1, n_1+n_2+n_3

        return n_1
