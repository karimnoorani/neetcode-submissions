class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w2) < len(w1) and w2[:minLen] == w1[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visiting = set()
        visited = set()
        res = []
        
        def dfs(c):
            if c in visiting:
                return False
            
            if c in visited:
                return True
            
            visiting.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visiting.remove(c)
            res.append(c)
            visited.add(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])