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
            cur = cur.children[c]
            cur.count += 1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie_obj = Trie()
        for word in strs:
            trie_obj.insert(word)
        
        cur = trie_obj.root
        for i in range(len(strs[0])):
            char = strs[0][i]
            if cur.children[char].count != len(strs):
                return strs[0][:i]
            cur = cur.children[char]
        
        return strs[0]
