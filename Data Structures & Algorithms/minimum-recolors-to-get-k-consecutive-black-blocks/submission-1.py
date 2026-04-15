class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = {'W': 0, 'B': 0}
        res = k

        for i in range(len(blocks)):
            freq[blocks[i]] += 1
            
            if i >= k:
                freq[blocks[i-k]] -= 1
            
            if i >= k-1:
                res = min(res, freq['W'])
        
        return res
