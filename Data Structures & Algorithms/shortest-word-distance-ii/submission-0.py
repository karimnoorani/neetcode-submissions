class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index = defaultdict(list)
        for i, s in enumerate(wordsDict):
            self.index[s].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        w1P = 0
        w2P = 0
        res = float('INF')
        while w1P < len(self.index[word1]) and w2P < len(self.index[word2]):
            res = min(res, abs(self.index[word1][w1P]-self.index[word2][w2P]))
            if self.index[word1][w1P] < self.index[word2][w2P]:
                w1P += 1
            else:
                w2P += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
