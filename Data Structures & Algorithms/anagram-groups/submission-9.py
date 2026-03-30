class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list) # character mapping -> word

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c)-ord('a')] += 1
            
            wordDict[tuple(count)].append(word)
        
        return list(wordDict.values())