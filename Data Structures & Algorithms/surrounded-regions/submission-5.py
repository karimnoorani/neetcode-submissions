class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(r, c, region):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return False
            
            if board[r][c] == 'X' or (r, c) in visited:
                return True

            visited.add((r, c))
            region.append((r, c))

            up = dfs(r-1, c, region)
            down = dfs(r+1, c, region)
            left = dfs(r, c-1, region)
            right = dfs(r, c+1, region)

            return up and down and left and right
        
        for r in range(ROWS):
            for c in range(COLS):
                region = []
                if board[r][c] != 'X' and (r, c) not in visited and dfs(r, c, region):
                    for i, j in region:
                        board[i][j] = 'X'