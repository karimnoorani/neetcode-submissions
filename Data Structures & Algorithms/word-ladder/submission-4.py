class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        neighbors = defaultdict(list)
        encodings = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                encoding = word[:i] + '*' + word[i+1:]
                encodings[word].append(encoding)
                neighbors[encoding].append(word)
        
        queue = deque([[beginWord, 1]])
        visited = set([beginWord])

        while queue:
            word, transformations = queue.popleft()

            if word == endWord:
                return transformations
            
            for encoding in encodings[word]:
                for nei in neighbors[encoding]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append([nei, transformations+1])
        
        return 0