class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        stack = []
        visited = set()
        
        def dfs(r, c, i):
            if i == len(word) and "".join(stack) == word:
                print("Found")
                return True
            
            if (min(r, c) < 0 or r == ROWS 
                or c == COLS or (r, c) in visited):
                return False

            if i >= len(word) or board[r][c] != word[i]:
                return False
            
            stack.append(board[r][c])
            visited.add((r,c))
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for neighbor in neighbors:
                nR, nC = neighbor
                if dfs(nR, nC, i+1):
                    return True
            
            stack.pop()
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
        