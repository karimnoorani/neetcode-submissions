class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def insertZeroes(r, c):
            for i in range(COLS):
                if matrix[r][i] != 0:
                    matrix[r][i] = '*'
            
            for i in range(ROWS):
                if matrix[i][c] != 0:
                    matrix[i][c] = '*'
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    insertZeroes(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == '*':
                    matrix[r][c] = 0