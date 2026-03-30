class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]
        
        if originalColor == color:
            return image
        
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != originalColor:
                return
            
            image[r][c] = color
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r+dR, c+dC)
        
        dfs(sr, sc)
        return image
            