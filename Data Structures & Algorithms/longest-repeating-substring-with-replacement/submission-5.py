class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxSeq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1)-max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maxSeq = max(maxSeq, r-l+1)
        
        return maxSeq