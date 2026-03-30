class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def doesExist(self, word: str, curr: TrieNode) -> bool:
        for i in range(len(word)):
            c = word[i]
            if c != '.':
                if c not in curr.children:
                    return False
                else:
                    curr = curr.children[c]
            else:
                for child in curr.children:
                    if self.doesExist(word[i+1:], curr.children[child]):
                        return True
                return False
        return curr.word

    def search(self, word: str) -> bool:
        return self.doesExist(word, self.root)
        