class Leaderboard:

    def __init__(self):
        self.data = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.data[playerId] += score

    def top(self, K: int) -> int:
        res = 0
        heap = []
        for playerId in self.data:
            res += self.data[playerId]
            heapq.heappush(heap, self.data[playerId])
            if len(heap) > K:
                res -= heapq.heappop(heap)
        
        return res

    def reset(self, playerId: int) -> None:
        self.data[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
