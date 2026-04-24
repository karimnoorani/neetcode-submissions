class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = Counter(s)
        res = []

        for i in range(len(order)):
            if order[i] not in chars:
                continue
            
            while chars[order[i]] > 0:
                res.append(order[i])
                chars[order[i]] -= 1
        
        for c in chars:
            while chars[c] > 0:
                res.append(c)
                chars[c] -= 1
        
        return "".join(res)