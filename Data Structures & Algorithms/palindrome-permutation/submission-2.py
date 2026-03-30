class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd = 0

        for c in count:
            if count[c] % 2 != 0:
                odd += 1
        
        return odd <= 1