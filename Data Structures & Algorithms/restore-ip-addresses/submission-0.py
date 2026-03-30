class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        cache = {}

        def dfs(i, breaks):
            if i == len(s) and breaks == 4:
                return [""]
            
            if i == len(s) or breaks == 4:
                return []

            if (i, breaks) in cache:
                return cache[(i, breaks)]
            
            res = []
            for j in range(i+1, min(i+4, len(s)+1)):
                part = s[i:j]
                if int(part) > 255 or (len(part) > 1 and part[0] == "0"):
                    continue
                for way in dfs(j, breaks+1):
                    res.append(part + "." + way if way != "" else part)
            cache[(i, breaks)] = res
            return cache[(i, breaks)]
        
        return dfs(0, 0)