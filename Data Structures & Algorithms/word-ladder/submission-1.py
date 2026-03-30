class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                adj[pattern].append(w)
        
        q = deque([beginWord])
        visited = set([beginWord])
        moves = 1

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return moves
                
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            moves += 1
        
        return 0