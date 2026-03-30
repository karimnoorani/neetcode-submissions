class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        
        for s in strs:
            res.append(str(len(s)))
            res.append('|')
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            numArr = []
            
            while s[i] != '|':
                print(s[i])
                numArr.append(s[i])
                i += 1
            i += 1

            wordLen = int("".join(numArr))
            res.append(s[i:i+wordLen])

            i += wordLen
        
        return res