class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        adjList = defaultdict(list)
        visiting = set()

        for a, b in similarPairs:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(s1, s2):
            if s1 == s2:
                return True
            
            if s1 in visiting:
                return False
            
            visiting.add(s1)
            for nei in adjList[s1]:
                if dfs(nei, s2):
                    visiting.remove(s1)
                    return True
            visiting.remove(s1)
            return False
        
        for s1, s2 in zip(sentence1, sentence2):
            if not dfs(s1, s2):
                return False
        
        return True