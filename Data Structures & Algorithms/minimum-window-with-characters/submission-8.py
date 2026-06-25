class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        tMap = Counter(t)
        sMap = defaultdict(int)
        left = 0
        result = ""
        resultLen = float('inf')

        for right in range(len(s)):
            sMap[s[right]] += 1
            count += 1 if sMap[s[right]] == tMap.get(s[right], 0) else 0

            while count == len(tMap):
                if right-left+1 < resultLen:
                    result = s[left:right+1]
                    resultLen = right-left+1
                
                sMap[s[left]] -= 1
                count += -1 if sMap[s[left]] < tMap.get(s[left], 0) else 0
                left += 1
        
        return result