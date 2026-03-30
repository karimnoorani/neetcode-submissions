class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            row = [1 for _ in range(i+1)]
            for j in range(1, i):
                row[j] = prev_row[j-1] + prev_row[j]
            prev_row = row
        
        return row