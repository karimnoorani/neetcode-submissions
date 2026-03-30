class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patternMap = defaultdict(list)
        wordToPatterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                
                patternMap[pattern].append(word)
                wordToPatterns[word].append(pattern)
        
        transf = 1
        q = deque([beginWord])
        visited = set([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return transf
                
                for pattern in wordToPatterns[word]:
                    for nei in patternMap[pattern]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        q.append(nei)
            transf += 1
        
        return 0