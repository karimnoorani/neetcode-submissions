class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        cnt = 0
        L = 0

        for R in range(len(fruits)):
            freq[fruits[R]] += 1
            cnt += 1 if freq[fruits[R]] == 1 else 0

            while cnt > 2:
                freq[fruits[L]] -= 1
                cnt += -1 if freq[fruits[L]] == 0 else 0
                L += 1
            
            res = max(res, R-L+1)
        
        return res