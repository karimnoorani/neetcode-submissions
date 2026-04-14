class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = []
        while i < len(chars):
            res.append(chars[i])
            length = 1
            j = i + 1

            while j < len(chars) and chars[i] == chars[j]:
                length += 1
                j += 1
            
            if length > 1:
                length = str(length)
                for c in length:
                    res.append(c)
            
            i = j
        
        for i in range(len(res)):
            chars[i] = res[i]
        
        return len(res)
        