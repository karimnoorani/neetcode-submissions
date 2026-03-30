class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = set()
        def updateZeroes(r, c):
            for i in range(len(matrix)):
                if matrix[i][c] != 0:
                    matrix[i][c] = 0
                    visited.add((i, c))
            for i in range(len(matrix[0])):
                if matrix[r][i] != 0:
                    matrix[r][i] = 0
                    visited.add((r, i))
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r, c) not in visited and matrix[r][c] == 0:
                    updateZeroes(r, c)

