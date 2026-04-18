class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        res = []
        freq = Counter(s)
        heap = []
        
        for c in freq:
            heapq.heappush(heap, [-freq[c], c])
        
        cooldown = deque() # [index, char]
        for i in range(len(s)):
            if cooldown and i == cooldown[0][0]:
                _, c = cooldown.popleft()
                heapq.heappush(heap, [-freq[c], c])
            
            if not heap:
                return ""
            
            count, c = heapq.heappop(heap)
            res.append(c)
            freq[c] -= 1

            if freq[c] > 0:
                cooldown.append([i+k, c])
        
        return "".join(res)