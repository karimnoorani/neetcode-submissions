class TrieNode:
    def __init__(self, word=False, count=0):
        self.children = {}
        self.word = False
        self.count = count

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.prefix = []
        for word, count in zip(sentences, times):
            self.addWord(word, count)
    
    def addWord(self, word, count=None):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        cur.count = count if count is not None else cur.count + 1

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.addWord("".join(self.prefix))
            self.prefix = []
            return []
        
        self.prefix.append(c)
        route = []
        cur = self.root
        for c in self.prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
            route.append(c)
        
        res = []
        def backtrack(node):
            if node.word:
                res.append((-node.count, "".join(route)))
            
            for c in node.children:
                route.append(c)
                backtrack(node.children[c])
                route.pop()
        
        backtrack(cur)
        res.sort()
        return [x[1] for x in res[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
