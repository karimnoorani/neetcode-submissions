class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        for followee in self.followMap[userId] | set([userId]):
            for tweet in self.tweetMap[followee]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        tweets = []
        while min_heap:
            _, tweetId = heapq.heappop(min_heap)
            tweets.append(tweetId)
        
        return tweets[::-1]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
