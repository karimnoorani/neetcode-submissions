class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstRow = False
        firstCol = False  # ✅ new flag

        # Check if first row or first column should be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] != 0:
                    continue

                if r == 0:
                    firstRow = True
                if c == 0:
                    firstCol = True

                matrix[r][0] = 0
                matrix[0][c] = 0

        # Zero cells based on markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero first row if needed
        if firstRow:
            for c in range(COLS):
                matrix[0][c] = 0

        # Zero first column if needed
        if firstCol:
            for r in range(ROWS):
                matrix[r][0] = 0
        