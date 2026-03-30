class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            right = dfs(r+1, c, i+1)
            up = dfs(r, c+1, i+1)
            left = dfs(r-1, c, i+1)
            down = dfs(r, c-1, i+1)
            visited.remove((r, c))

            return right or up or left or down
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False