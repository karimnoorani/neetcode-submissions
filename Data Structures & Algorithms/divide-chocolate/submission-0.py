class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canCut(minTotal):
            piece = 0
            chunks = 0
            for c in sweetness:
                piece += c
                if piece >= minTotal:
                    chunks += 1
                    piece = 0
            return chunks >= k+1
        
        L, R = 1, sum(sweetness)
        res = 1
        while L <= R:
            M = (L + R) // 2

            if canCut(M):
                res = M
                L = M + 1
            else:
                R = M - 1
        return res