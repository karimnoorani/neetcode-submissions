class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        res = 0

        for i in range(N):
            res += mat[i][i]
        
        for i in range(N):
            if i != N-i-1:
                res += mat[i][N-i-1]
        
        return res