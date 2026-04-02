class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = ''
        even = ''
        for c in freq:
            if freq[c] % 2 == 1 and (odd == '' or freq[c] > freq[odd]):
                odd = c
            elif freq[c] % 2 == 0 and (even == '' or freq[c] < freq[even]):
                even = c
        return freq[odd]-freq[even]