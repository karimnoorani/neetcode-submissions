class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie(words).root
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        path = []
        def dfs(r, c, root):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS 
                or (r, c) in visited or board[r][c] not in root.children):
                return
            
            if root.children[board[r][c]].word:
                res.add("".join(path + [board[r][c]]))
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            
            visited.add((r, c))
            path.append(board[r][c])
            for n in neighbors:
                dfs(n[0], n[1], root.children[board[r][c]])
            path.pop()
            visited.remove((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return list(res)