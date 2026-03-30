class Leaderboard:

    def __init__(self):
        self.data = defaultdict(int)
        self.heap = []

    def addScore(self, playerId: int, score: int) -> None:
        self.data[playerId] += score
        heapq.heappush(self.heap, [-self.data[playerId], playerId])

    def top(self, K: int) -> int:
        res = 0
        heap = self.heap[:]
        seen = set()
        while heap and K > 0:
            score, playerid = heapq.heappop(heap)
            score *= -1
            if playerid not in seen and self.data[playerid] == score:
                res += score
                seen.add(playerid)
                K -= 1
        
        return res

    def reset(self, playerId: int) -> None:
        self.data[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
