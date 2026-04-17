class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        lengthToWord = defaultdict(set)
        lengths = set()
        for w in words:
            l = len(w)
            lengthToWord[l].add(w)
            lengths.add(l)
        
        isBold = [False] * len(s)

        for l in lengths:
            for i in range(len(s)-l+1):
                if s[i:i+l] in lengthToWord[l]:
                    for j in range(i, i+l):
                        isBold[j] = True
        
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
