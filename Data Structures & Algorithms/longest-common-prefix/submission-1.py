class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        validPrefix = True
        i = 0

        while validPrefix:
            if i >= len(strs[0]):
                break
            prefix = strs[0][i]
            
            for s in strs:
                if i >= len(s) or s[i] != prefix:
                    validPrefix = False
                    break
            
            if validPrefix:
                i += 1
        
        return strs[0][:i]