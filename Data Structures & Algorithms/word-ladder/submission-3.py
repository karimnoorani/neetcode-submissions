class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        wordToPats = defaultdict(list)
        patsToWords = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                wordToPats[word].append(pattern)
                patsToWords[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        trans = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return trans

                for pattern in wordToPats[word]:
                    for nei in patsToWords[pattern]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(nei)
            trans += 1
        
        return 0


