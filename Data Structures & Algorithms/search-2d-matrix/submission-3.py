class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def getMid(l, r):
            point = (r[0]*COLS)+(l[0]*COLS)+r[1]+l[1]
            return (point//COLS, point % COLS)

        def getNextPoint(matrix, r, c):
            if c < 0:
                return (r-1, COLS-1)
            elif c >= COLS:
                return (r+1, 0)
            else:
                return (r, c)
        
        l, r = (0, 0), (ROWS-1, COLS-1)

        while (r[0]*COLS+r[1]) >= (l[0]*COLS+l[1]):
            mid = getMid(l, r)
            print(mid)

            if target > matrix[mid[0]][mid[1]]:
                l = getNextPoint(matrix, mid[0], mid[1]+1)
            elif target < matrix[mid[0]][mid[1]]:
                r = getNextPoint(matrix, mid[0], mid[1]-1)
            else:
                return True
            
        return False