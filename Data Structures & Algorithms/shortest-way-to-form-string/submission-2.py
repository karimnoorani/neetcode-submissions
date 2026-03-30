class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not set(target).issubset(set(source)):
            return -1
        
        i, res = 0, 0
        while i < len(target):
            j = 0
            res += 1
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                j += 1
        
        return res