class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = float('-inf')
        even = float('inf')
        for c in freq:
            if freq[c] % 2 == 1 and freq[c] > odd:
                odd = freq[c]
            elif freq[c] % 2 == 0 and freq[c] < even:
                even = freq[c]
        return odd-even