class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}|")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != '|':
                length = length*10+int(s[i])
                i += 1
            i += 1 # skipping |

            res.append(s[i:i+length])
            i += length
        
        return res