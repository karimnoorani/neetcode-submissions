class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[float('INF') for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                newMatrix[c][r] = matrix[r][c]
        
        return newMatrix