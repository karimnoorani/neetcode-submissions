class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        for s in strings:
            cMap = [0]
            firstChar = s[0]
            for c in s[1:]:
                cMap.append((ord(c)-ord(firstChar))%26)
            
            charMap[tuple(cMap)].append(s)
        
        return list(charMap.values())