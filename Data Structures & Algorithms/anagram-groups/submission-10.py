class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = defaultdict(list)

        for s in strs:
            charMap = [0] * 26
            for c in s:
                charMap[ord(c)-ord('a')] += 1
            
            sMap[tuple(charMap)].append(s)
        
        return list(sMap.values())