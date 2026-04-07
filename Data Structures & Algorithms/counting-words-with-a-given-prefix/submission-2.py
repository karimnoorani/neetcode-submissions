class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur.children[c].count += 1
            cur = cur.children[c]
    
    def getCount(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        Tree = Trie()
        for w in words:
            Tree.insert(w[:len(pref)])
        return Tree.getCount(pref)