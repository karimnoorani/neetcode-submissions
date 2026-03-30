class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        extraCharUsed = False if len(s) % 2 == 1 else True
        
        for c in count:
            if count[c] % 2 != 0:
                if extraCharUsed:
                    return False
                extraCharUsed = True
        
        return True