class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0

        sub = set()
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                longest = max(longest, len(sub))
                r += 1
            else:
                while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
        return longest
            