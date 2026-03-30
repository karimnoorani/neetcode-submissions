class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False
        
        similarity = set()
        for x, y in similarPairs:
            similarity.add((x, y))
            similarity.add((y, x))
        
        for i in range(len(s1)):
            if s1[i] == s2[i] or (s1[i], s2[i]) in similarity:
                continue
            
            return False

        return True