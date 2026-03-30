class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.word
            
            if word[i] == '.':
                for child in cur.children:
                    if dfs(i+1, cur.children[child]):
                        return True
                return False
            
            if word[i] not in cur.children:
                return False
            else:
                return dfs(i+1, cur.children[word[i]])
        
        return dfs(0, self.root)