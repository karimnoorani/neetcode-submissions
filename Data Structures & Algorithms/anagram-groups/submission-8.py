class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)

        for s in strs:
            charList = [0] * 26
            
            for c in s:
                charList[ord(c) - ord('a')] += 1
            
            charMap[tuple(charList)].append(s)
            
        return list(charMap.values())