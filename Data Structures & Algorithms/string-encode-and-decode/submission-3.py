class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + '|' + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            print(res)
            numString = []
            
            while s[i] != '|':
                numString.append(s[i])
                i += 1

            i += 1 # Skipping over |

            numString = "".join(numString)

            numToIterate = int(numString)
            
            res.append(s[i:i+numToIterate])

            i += numToIterate
        
        return res