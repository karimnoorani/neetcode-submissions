class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        
        subStr = 0
        chars = set()

        for c in s:
            count[c] -= 1
            subStr += 1
            chars.add(c)

            if count[c] == 0:
                chars.remove(c)
            
            if len(chars) == 0:
                res.append(subStr)
                subStr = 0
        
        return res