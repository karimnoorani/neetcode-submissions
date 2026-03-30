class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, (ROWS * COLS)-1

        while L <= R:
            M = (L+R) // 2
            
            r, c = M//COLS, M%COLS

            if matrix[r][c] > target:
                R = M - 1
            elif matrix[r][c] < target:
                L = M + 1
            else:
                return True
        
        return False