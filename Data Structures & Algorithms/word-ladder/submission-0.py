class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q = deque()
        visited = set()

        q.append(beginWord)
        
        def isValidTrans(start, end):
            diff = 0
            for i in range(len(start)):
                if start[i] != end[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        moves = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return moves
                
                for word in wordList:
                    if word not in visited and isValidTrans(w, word):
                        q.append(word)
                        visited.add(word)
            moves += 1
        
        return 0