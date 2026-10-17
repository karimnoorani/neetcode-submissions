class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = [0] * 26
        count_t = [0] * 26

        for char_s, char_t in zip(s, t):
            count_s[ord(char_s)-ord('a')] += 1
            count_t[ord(char_t)-ord('a')] += 1
        
        return count_s == count_t