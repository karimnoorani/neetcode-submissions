class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = Counter(s)
        keys = set(chars.keys())
        res = []

        for i in range(len(order)):
            if order[i] not in chars:
                continue
            
            while chars[order[i]] > 0:
                res.append(order[i])
                chars[order[i]] -= 1
            keys.remove(order[i])
        
        for c in keys:
            while chars[c] > 0:
                res.append(c)
                chars[c] -= 1
        
        return "".join(res)