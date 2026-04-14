class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])
        
        res = []
        for c in range(COLS):
            row = []
            for r in range(ROWS-1, -1, -1):
                row.append(boxGrid[r][c])
            res.append(row)
        
        for c in range(ROWS):
            empty_pos = COLS-1
            for r in range(COLS-1, -1, -1):
                if res[r][c] == '*':
                    empty_pos = r - 1
                elif res[r][c] == '#':
                    res[r][c], res[empty_pos][c] = res[empty_pos][c], res[r][c]
                    empty_pos -= 1
        
        return res