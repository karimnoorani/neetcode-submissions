class TrieNode:
    def __init__(self):
        self.children = {}
        self.folder = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertFolder(self, folder):
        curr = self.root
        for f in folder.split('/')[1:]:
            if f not in curr.children:
                curr.children[f] = TrieNode()
            curr = curr.children[f]
        curr.folder = True
    
    def isSubFolder(self, folder):
        curr = self.root
        for f in folder.split('/')[1:]:
            if curr.folder:
                return True
            curr = curr.children[f]
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        Tree = Trie()
        res = []
        
        for f in folder:
            Tree.insertFolder(f)
        
        for f in folder:
            if not Tree.isSubFolder(f):
                res.append(f)
        
        return res