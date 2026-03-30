class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        prevRow = [0] * (COLS-1)
        prevRow.append(1)

        for r in range(ROWS-1, -1, -1):
            curRow = [0] * COLS
            curRow[-1] = prevRow[-1] if obstacleGrid[r][-1] != 1 else 0
            for c in range(COLS-2, -1, -1):
                curRow[c] = curRow[c+1] + prevRow[c] if obstacleGrid[r][c] != 1 else 0
            print(curRow)
            prevRow = curRow
        
        return curRow[0]