'''
time = int
tweetMap = {} - userId -> List[tweets]
followMap = {} - userId -> Set(userId)
'''
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId not in self.followMap[userId]:
            self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            for tweetInfo in self.tweetMap[followeeId]:
                heapq.heappush(heap, tweetInfo)
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(reverse=True)
        return [tweet[1] for tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
