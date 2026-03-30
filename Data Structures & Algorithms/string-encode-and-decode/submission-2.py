class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s))
            res += '|'
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        num = ""
        while i < len(s):
            if s[i] != '|':
                num += s[i]
                i += 1
            else:
                num = int(num)
                res.append(s[i+1:i+num+1])
                i += num + 1
                num = ""

        return res