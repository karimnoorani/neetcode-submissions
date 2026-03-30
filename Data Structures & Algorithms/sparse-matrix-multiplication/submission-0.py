class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])

        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for p in range(k):
                    res[i][j] += mat1[i][p] * mat2[p][j]
        
        return res