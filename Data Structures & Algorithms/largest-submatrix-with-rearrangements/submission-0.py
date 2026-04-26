class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        prev_row = [0 for _ in range(COLS)]
        res = 0
        
        for row in matrix:
            cur_row = [0 for _ in range(COLS)]
            for c in range(COLS):
                if row[c] > 0:
                    cur_row[c] = prev_row[c]+1
            
            sorted_row = sorted(cur_row, reverse=True)
            for c in range(COLS):
                res = max(res, (c+1)*sorted_row[c])
            
            prev_row = cur_row
        
        return res