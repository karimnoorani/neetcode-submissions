class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstCol = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    continue
                
                if c == 0:
                    firstCol = True
                else:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for c in range(1, len(matrix[0])):
            if matrix[0][c] != 0:
                continue
            
            for r in range(1, len(matrix)):
                matrix[r][c] = 0
        
        for r in range(len(matrix)):
            if matrix[r][0] != 0:
                continue
            
            for c in range(1, len(matrix[0])):
                matrix[r][c] = 0
        
        if firstCol:
            for r in range(len(matrix)):
                matrix[r][0] = 0