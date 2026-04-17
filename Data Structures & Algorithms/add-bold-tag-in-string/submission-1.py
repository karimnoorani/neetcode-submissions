class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        isBold = [False] * len(s)
        
        for w in words:
            start = s.find(w)
            while start != -1:
                for i in range(len(w)):
                    isBold[start+i] = True
                start = s.find(w, start+1)
        
        res = []
        i = 0

        while i < len(s):
            if not isBold[i]:
                res.append(s[i])
                i += 1
            else:
                res.append('<b>')
                while i < len(s) and isBold[i]:
                    res.append(s[i])
                    i += 1
                res.append('</b>')
        
        return "".join(res)
