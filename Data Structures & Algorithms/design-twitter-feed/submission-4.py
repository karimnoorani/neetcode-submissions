class Twitter:

    def __init__(self):
        self.userFollowMap = {} # userId -> set() containing followeeids
        self.userTweetMap = {} # userId -> list
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userFollowMap:
            self.userFollowMap[userId] = set([userId])
        
        if userId not in self.userTweetMap:
            self.userTweetMap[userId] = []
        
        self.userTweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for followee in self.userFollowMap[userId]:
            res = res + self.userTweetMap[followee]
        res.sort(reverse=True)
        values = []
        for item in res:
            values.append(item[1])
        return values[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowMap:
            self.userFollowMap[followerId] = set([followerId])
        
        if followerId not in self.userTweetMap:
            self.userTweetMap[followerId] = []
        
        self.userFollowMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.userFollowMap[followerId]:
            return
        self.userFollowMap[followerId].remove(followeeId)
