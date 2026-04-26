class Solution:
    def encode(self, s: str) -> str:
        res = []
        i = 0

        while i < len(s):
            start = i

            while i < len(s) and s[start] == s[i]:
                i += 1
            
            encoded = f'{i-start}[{s[start]}]'
            if len(encoded) < i-start:
                res.append(encoded)
            else:
                res.append("".join(s[start:i]))
        
        return "".join(res)