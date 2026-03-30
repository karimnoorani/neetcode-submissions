class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for i, c in enumerate(order):
            orderDict[c] = i
        
        def areSorted(word1, word2):
            for i in range(max(len(word1), len(word2))):
                if i == len(word1):
                    return True
                
                if i == len(word2):
                    return False
                
                if orderDict[word1[i]] < orderDict[word2[i]]:
                    return True

                if orderDict[word2[i]] < orderDict[word1[i]]:
                    return False
            
            return True

        for i in range(len(words)-1):
            print(words[i], words[i+1])
            if not areSorted(words[i], words[i+1]):
                return False
        
        return True